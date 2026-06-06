# Relative Path Migration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use subagent-driven-development or executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 将数据库中 `readme_path` / `readme_zh_path` 从绝对路径（Windows/Linux 混用）统一迁移为相对路径（纯文件名），并更新所有相关代码逻辑。

**Architecture:** 数据库只存文件名，文件读写通过 `get_readme_dir() + filename` 拼接完整路径。新增迁移函数在 `init_db()` 中自动执行，兼容跨平台历史数据。

**Tech Stack:** Python, sqlite3, os.path

---

## Files Modified

| File | Change |
|------|--------|
| `db.py` | Add `migrate_paths()`, call in `init_db()` |
| `fetch.py` | Modify `fetch_readme()` to return filename only |
| `translator.py` | Fix file I/O: join with `get_readme_dir()` before reading; pass filename to DB |

---

## Files NOT Modified (Justified)

| File | Reason |
|------|--------|
| `server.py` | API `/api/repos/:id/readme*` 已用 full_name 生成文件名；`make_relative_path()` 迁移后自动正确返回（DB 值已是纯文件名，不匹配路径前缀，进入 basename 分支直接返回） |
| `db.py upsert_repo()` | 接收什么存什么，上游改为传 filename 即可 |
| `web/app.js` | 从未直接使用 readme_path/readme_zh_path 字段 |

---

### Task 1: db.py — Add migration function and integrate into init_db()

**Files:**
- Modify: `db.py`

- [ ] **Step 1: Add migrate_paths() function after get_connection()**

Add this function at line ~87 (after `init_db()` ends):

```python
def migrate_paths():
    """将 readme_path/readme_zh_path 从绝对路径迁移为相对路径（文件名）"""
    conn = get_connection()
    cursor = conn.execute('SELECT id, readme_path, readme_zh_path FROM repositories')
    
    for row in cursor:
        repo_id, rp, rzp = row[0], row[1], row[2]
        
        updates = []
        # 已迁移的路径就是纯文件名（不含路径分隔符），跳过
        if rp and ('/' in str(rp) or '\\' in str(rp)):
            updates.append(('readme_path', os.path.basename(str(rp))))
        if rzp and ('/' in str(rzp) or '\\' in str(rzp)):
            updates.append(('readme_zh_path', os.path.basename(str(rzp))))
        
        if updates:
            for field, value in updates:
                conn.execute(f'UPDATE repositories SET {field} = ? WHERE id = ?', (value, repo_id))
    
    conn.commit()
```

- [ ] **Step 2: Call migrate_paths() at the end of init_db()**

In `init_db()` function, add this line right before `conn.close()` on line ~86:

```python
    migrate_paths()
    conn.commit()
    conn.close()
```

The final lines of `init_db()` should be:
```python
        conn.execute('CREATE INDEX IF NOT EXISTS idx_translate_status ON repositories(translate_status)')
        conn.execute('CREATE INDEX IF NOT EXISTS idx_is_read ON repositories(is_read)')
    
    conn.commit()
    migrate_paths()  # Add this line
    conn.close()
```

- [ ] **Step 3: Verify migration works**

Run:
```bash
cd /mnt/e/Projects/htmlSpace/GithubAssistant && python3 -c "from db import get_connection; conn = get_connection(); rows = conn.execute('SELECT id, full_name, readme_path FROM repositories LIMIT 5').fetchall(); [print(r) for r in rows]; conn.close()"
```

Expected: `readme_path` should now be filenames like `owner__repo.md`, not absolute paths.

- [ ] **Step 4: Commit**

```bash
git add db.py
git commit -m "fix: migrate readme paths to relative filenames"
```

---

### Task 2: fetch.py — Modify fetch_readme() to return filename only

**Files:**
- Modify: `fetch.py`

- [ ] **Step 1: Change return value of fetch_readme()**

On line ~132, change:
```python
    logger.info(f'{full_name} README 已保存到 {filepath}')
    return filepath
```

To:
```python
    logger.info(f'{full_name} README 已保存到 {filepath}')
    return filename
```

- [ ] **Step 2: Verify fetch.py logic**

The `run_fetch()` function calls `fetch_readme()` and passes the result to `upsert_repo()`. Since `upsert_repo()` stores whatever it receives, returning `filename` means DB will now store filenames. File is still saved correctly at full path (`filepath`).

- [ ] **Step 3: Commit**

```bash
git add fetch.py
git commit -m "fix: return filename from fetch_readme() for relative path storage"
```

---

### Task 3: translator.py — Fix file I/O to use joined paths

**Files:**
- Modify: `translator.py`

- [ ] **Step 1: Fix translate_single_repo() file reading**

In `translate_single_repo()` function, around line ~109, change:
```python
    try:
        with open(repo['readme_path'], 'r', encoding='utf-8') as f:
            readme_content = f.read()
```

To:
```python
    try:
        full_readme_path = os.path.join(readme_dir, repo['readme_path'])
        with open(full_readme_path, 'r', encoding='utf-8') as f:
            readme_content = f.read()
```

- [ ] **Step 2: Fix run_translate() file reading**

In `run_translate()` function, around line ~177, change:
```python
        try:
            with open(repo['readme_path'], 'r', encoding='utf-8') as f:
                readme_content = f.read()
```

To:
```python
        try:
            full_readme_path = os.path.join(readme_dir, repo['readme_path'])
            with open(full_readme_path, 'r', encoding='utf-8') as f:
                readme_content = f.read()
```

- [ ] **Step 3: Verify translator.py logic**

The `zh_filepath` is already constructed correctly on line ~117/185 using `os.path.join(readme_dir, zh_filename)`. The `update_translate_status()` call passes this full path — but we need to ensure only the filename is stored in DB. 

Actually, looking at line ~122 and ~190:
```python
        update_translate_status(repo_id, 'done', readme_zh_path=zh_filepath)
```

This `zh_filepath` is already a full path. We should extract just the filename before passing to DB. Change these lines to:
```python
        update_translate_status(repo_id, 'done', readme_zh_path=zh_filename)
```

Where `zh_filename = repo_to_filename_zh(full_name)` (already defined on line ~116/184).

- [ ] **Step 4: Commit**

```bash
git add translator.py
git commit -m "fix: use joined paths for file I/O in translator"
```

---

## Verification Steps

After all tasks are complete, run these commands to verify:

```bash
cd /mnt/e/Projects/htmlSpace/GithubAssistant

# 1. Check DB has relative paths
python3 -c "from db import get_connection; conn = get_connection(); rows = conn.execute('SELECT id, full_name, readme_path, readme_zh_path FROM repositories LIMIT 5').fetchall(); [print(r) for r in rows]; conn.close()"

# Expected output:
# (1, 'repo/name', 'name__repo.md', 'name__repo_zh.md')

# 2. Test server starts without errors
python3 -c "from server import app; print('Server imports OK')"

# 3. Verify file operations work
python3 -c "
from utils import get_readme_dir, repo_to_filename
import os
readme_dir = get_readme_dir()
filename = 'owner__repo.md'
full_path = os.path.join(readme_dir, filename)
print(f'readme_dir: {readme_dir}')
print(f'filename: {filename}')
print(f'full_path: {full_path}')
"
```

---

## Impact Summary

| Component | Before | After |
|-----------|--------|-------|
| DB storage | `E:\Projects\...\owner__repo.md` | `owner__repo.md` |
| fetch.py return | Full filepath | Filename only |
| translator.py I/O | Direct path from DB | Joined with get_readme_dir() |
| server.py API | Already uses full_name to construct paths | No change needed |
| Frontend app.js | Never touched these fields | No change needed |
