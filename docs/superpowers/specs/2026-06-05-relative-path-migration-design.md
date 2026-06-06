# Design: readme_path/readme_zh_path 相对化改造

## Background

数据库中 `readme_path` / `readme_zh_path` 当前存储 Windows/Linux 混用绝对路径，跨平台操作时产生歧义。需统一为相对路径（即文件名），所有文件读取通过 `get_readme_dir()` + filename 拼接还原完整路径。

## Scope

- **涉及字段**：`repositories.readme_path`, `repositories.readme_zh_path`
- **数据量**：~1179 条记录，6 条空值可跳过

---

## Changes

### 1. fetch.py — `fetch_readme()` (line ~132)

```python
# Before: return filepath          # E:\...\owner__repo.md
# After:  return filename           # owner__repo.md
return filename
```

`run_fetch()` 中写入数据库时已用此返回值，改为文件名即可。文件本身仍保存到完整路径（`get_readme_dir() + filename`），只是传给 DB 的是文件名部分。

### 2. translator.py — 文件读写 (line ~108, ~176)

当前代码直接用 `repo['readme_path']` 打开/写入文件，迁移后需拼接完整路径：

```python
# Before:
with open(repo['readme_path'], 'r') as f: ...
with open(zh_filepath, 'w') as f: ...   # zh_filepath is already full path

# After:
full_readme = os.path.join(get_readme_dir(), repo['readme_path'])
with open(full_readme, 'r') as f: ...
```

`update_translate_status()` 传入的 `readme_zh_path` 参数改为文件名（已符合）。

### 3. server.py — API 文件读取 (line ~75-99)

当前 `/api/repos/:id/readme` 和 `/api/repos/:id/readme_zh` 已从 full_name 重新生成完整路径，**无需改动**。

`make_relative_path()` 函数（line 17）在 `get_repos` API 中用于将绝对路径转相对路径返回前端。迁移后数据库已存文件名，此逻辑可简化为直接返回原值：

```python
def make_relative_path(abs_path):
    if not abs_path:
        return None
    # 已是相对路径（文件名），直接返回
    return os.path.basename(abs_path) if '/' in str(abs_path) or '\\' in str(abs_path) else abs_path
```

### 4. db.py — `upsert_repo()` (line ~96-138)

无需改动。该函数接收什么就存什么，上游改为传文件名即可。

---

## Migration Script

在 server.py 启动前或单独脚本中执行：

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

在 `init_db()` 末尾调用，确保每次启动时自动修复未迁移记录。

---

## Impact Summary

| Component | Before | After |
|-----------|--------|-------|
| DB storage | Absolute path (`E:\...\owner__repo.md`) | Filename only (`owner__repo.md`) |
| fetch.py `fetch_readme()` | Returns full filepath | Returns filename |
| translator.py file I/O | Directly uses `readme_path` value | Joins with `get_readme_dir()` first |
| server.py API `/api/repos/:id/readme*` | Already constructs from full_name | No change needed |
| Frontend app.js | Never touched these fields directly | No change needed |
