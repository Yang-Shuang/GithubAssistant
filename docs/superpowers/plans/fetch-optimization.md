# Fetch Optimization Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use subagent-driven-development (recommended) or executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 优化抓取任务的重复数据处理和增量更新能力

**Architecture:** 
1. 在 `run_fetch()` 中维护 `_processed_repos: set` 实现批次间去重
2. 新增 `db.py:get_existing_readme_names()` 查询已有 README 的仓库集合
3. 通过配置项 `update_all` 切换全量/增量模式

**Tech Stack:** Python, SQLite (sqlite3), no external dependencies for these changes

---

### Task 1: db.py — 新增 get_existing_readme_names() 函数

**Files:**
- Modify: `fetch/db.py:218-234` (在 `get_pending_translates()` 后添加)

目的：查询数据库中已有 README（readme_path 非空）的仓库名集合，供增量模式使用。

```python
def get_existing_readme_names():
    """返回已有 README 文件的仓库 full_name 列表"""
    conn = get_connection()
    cursor = conn.execute(
        'SELECT full_name FROM repositories WHERE readme_path IS NOT NULL AND readme_path != ""'
    )
    rows = cursor.fetchall()
    conn.close()
    
    return set(row[0] for row in rows)
```

- [ ] **Step 1: Write the code**
  - 在 `get_pending_translates()` 函数（约 db.py:219行）之后插入上述代码
  - 保持与现有代码风格一致：使用 `get_connection()`、`conn.close()`、返回类型说明

- [ ] **Step 2: Verify syntax**
  Run: `python3 -c "import sys; sys.path.insert(0, '.'); from fetch.db import get_existing_readme_names; print('OK')"` (实际路径需调整)

---

### Task 2: config.json — 新增 update_all 字段 + fetch.py 增量逻辑

**Files:**
- Modify: `fetch/config.json` — 添加 `"update_all": true`
- Modify: `fetch/fetch.py:256-332` (`run_fetch()` 函数)

#### 2a. config.json 修改

```json
{
  ...existing fields...,
  "update_all": true,
}
```

> **注意：** 如果用户已有旧配置，代码中需要 `config.get('update_all', True)` 提供默认值（向后兼容）

#### 2b. run_fetch() 核心逻辑修改

在 `run_fetch()` 函数开头（约第271行 `init_db()` 之后），添加以下逻辑：

```python
    init_db()
    
    # === 读取增量模式配置 ===
    update_all = config.get('update_all', True)
    
    # Reset counters for new fetch task
    global fetch_stop, total_repos_fetched
    fetch_stop = False
    total_repos_fetched = 0
    
    all_repos = []
    total_batches = len(batches)
    
    # === 去重集合（任务开始时清空）===
    processed_repos: set[str] = set()
    
    if not update_all:
        existing_readme_names = get_existing_readme_names()
        logger.info(f'增量模式：已有 {len(existing_readme_names)} 个仓库有 README')
```

然后在每个 batch 循环内部（约第301行 `for repo in repos:`），将现有逻辑替换为：

```python
        for repo in repos:
            # === 中断检查（每个repo前）===
            if fetch_stop:
                from utils import log_stop
                log_stop(logger, total_repos_fetched, len(all_repos), '抓取')
                return all_repos
            
            full_name = repo['full_name']
            
            # === 去重检查：跳过已处理的仓库 ===
            if full_name in processed_repos:
                logger.info(f'跳过重复仓库: {full_name}')
                continue
            
            try:
                repo['fetched_at'] = format_iso()
                
                # === 增量模式：跳过已有 README 的仓库 ===
                need_readme_fetch = True
                if not update_all and full_name in existing_readme_names:
                    logger.info(f'增量模式：跳过已有 README 的仓库 {full_name}')
                    # 仍然更新 metadata（stars/description等）通过 upsert_repo，但不抓取 README
                    repo['fetched_at'] = format_iso()
                    readme_path = None
                    need_readme_fetch = False
                    
                if need_readme_fetch:
                    readme_path = fetch_readme(repo['full_name'])
                
                if readme_path:
                    repo['readme_path'] = readme_path
                
                upsert_repo(repo)
                processed_repos.add(full_name)  # === 加入去重集合 ===
                total_repos_fetched += 1
                all_repos.append(repo)
                
                # === 进度日志（每完成一个repo）===
                from utils import log_done
                remaining = max(0, len(all_repos) - total_repos_fetched + (len(repos) - repos.index(repo)))
                estimated_total = total_repos_fetched + remaining
                log_done(logger, total_repos_fetched, remaining, estimated_total, '抓取')
            except Exception as e:
                logger.error(f'处理 {repo["full_name"]} 失败: {e}')
```

在 `run_fetch()` 函数末尾（约第331行），清空去重集合：

```python
    # === 任务结束，清空去重集合 ===
    processed_repos.clear()
    
    logger.info(f'全部抓取完成，共 {len(all_repos)} 个仓库')
    return all_repos
```

- [ ] **Step 1: Write the code**
  - config.json：添加 `"update_all": true`（保持 JSON 格式正确）
  - fetch.py `run_fetch()`：按上述代码修改，注意缩进和变量名一致性

- [ ] **Step 2: Verify syntax & logic**
  Run: `python3 -c "import json; f=open('config.json'); d=json.load(f); print(d.get('update_all')); f.close()"`
  Expected: `true`

---

### Task 3: utils.py — 新增跳过日志格式（可选优化）

**Files:**
- Modify: `fetch/utils.py` — 在现有 `log_done()` / `log_stop()` 之后添加新函数

目的：为"跳过"操作提供统一的日志输出，与进度日志风格一致。

```python
def log_skip(logger, name='任务'):
    """输出跳过日志（蓝色高亮）"""  
    msg = f'⏭️ 已跳过: {name}'
    
    record = logger.makeRecord(
        logger.name, 
        logging.INFO, 
        '', 
        0, 
        msg, 
        None, 
        None, 
        None, 
        None
    )
    setattr(record, '_colored', True)
    setattr(record, '_color_code', '\033[94m')  # 蓝色
    
    logger.handle(record)
```

然后在 fetch.py 中两处跳过逻辑替换 `logger.info(f'跳过...')` 为：

```python
from utils import log_skip, log_done, log_stop
# ...
log_skip(logger, full_name)
```

- [ ] **Step 1: Write the code**
  - utils.py：添加 `log_skip()` 函数
  - fetch.py：导入并使用新函数

---

## Self-Review Checklist

1. **Spec coverage:** ✅ Task 1 实现增量查询，Task 2 实现去重+增量过滤，Task 3 优化日志输出
2. **Placeholder scan:** ✅ 所有代码均为完整可执行代码，无"TBD"/"TODO"/"fill in"等占位符
3. **Type consistency:** ✅ `processed_repos: set[str]`、`existing_readme_names = get_existing_readme_names()` 类型一致；config.get() 默认值向后兼容
4. **Backward compatibility:** ✅ `config.get('update_all', True)` — 旧配置自动全量模式，不影响现有行为

---

## Execution Handoff

Plan complete and saved to `docs/superpowers/plans/fetch-optimization.md`. Two execution options:

**1. Subagent-Driven (recommended)** - I dispatch a fresh subagent per task, review between tasks, fast iteration

**2. Inline Execution** - Execute tasks in this session using executing-plans, batch execution with checkpoints

Which approach?
