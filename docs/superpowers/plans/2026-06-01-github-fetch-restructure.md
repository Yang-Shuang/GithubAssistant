# GitHub 抓取逻辑重构 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use subagent-driven-development (recommended) or executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 将抓取逻辑从"每个关键词单独搜索一次"改为"OR拼接批量搜索+自动翻页"，减少重复数据、优化 API 调用效率。

**Architecture:** 新增 `build_search_query()` 和 `fetch_repos_with_pagination()` 函数重构核心抓取流程；`run_fetch()` 适配新逻辑；config.json 新增配置项。keywords.json 独立读取，与 config.json keywords 解耦。

**Tech Stack:** Python 3.x, requests, SQLite (via existing db.py)

---

## Task 1: 更新配置文件

**Files:**
- Modify: `config.json`

- [ ] **Step 1: 添加新配置项到 config.json**

```json
{
  "github_token": "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",
  "keywords": ["vibe coding", "ai coding", "agent", "skill", "mcp server", "claude code", "opencode"],
  "fetch_top_n": 20,
  "request_interval": 0.5,
  "auto_translate": false,
  "llama_cpp": {
    "base_url": "http://localhost:9898",
    "model": "Qwen3.6-35B-A3B",
    "max_tokens": 153600
  },
  "translate_chunk_size": 20000,
  "max_q_length": 480,
  "page_size": 80,
  "min_stars_stop": 1000
}
```

- [ ] **Step 2: Commit**

```bash
git add config.json
git commit -m "chore: 添加抓取配置项 max_q_length/page_size/min_stars_stop"
```

---

## Task 2: 新增 keywords.json 读取函数

**Files:**
- Modify: `config.py`

- [ ] **Step 1: 在 config.py 末尾添加 load_keywords() 函数**

```python
def load_keywords():
    """从 keywords.json 加载关键词列表，返回 key 值数组"""
    kw_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'keywords.json')
    with open(kw_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return [kw['key'] for kw in data.get('keywords', [])]
```

- [ ] **Step 2: Commit**

```bash
git add config.py
git commit -m "feat: 添加 load_keywords() 函数读取 keywords.json"
```

---

---

## Task 3: 新增带翻页的搜索函数

**Files:**
- Modify: `fetch.py`

- [ ] **Step 1: 在 search_repos() 之后新增 fetch_repos_with_pagination() 函数**

```python
def fetch_repos_with_pagination(query, page_size=80, min_stars_stop=1000):
    """
    使用 OR 拼接的查询参数，分页搜索 GitHub 仓库。
    
    - 按 stars 降序排序
    - 翻页直到：任意仓库 stars < min_stars_stop，或返回结果数 < page_size
    
    Returns: list[dict] 去重后的仓库列表
    """
    config = load_config()
    token = config.get('github_token', '')
    headers = {'Authorization': f'token {token}'} if token else {}
    
    url = 'https://api.github.com/search/repositories'
    seen_repos = set()  # 用于去重（同一仓库可能在不同批次出现）
    all_repos = []
    page = 1
    
    while True:
        params = {
            'q': query,
            'sort': 'stars',
            'order': 'desc',
            'per_page': page_size,
            'page': page
        }
        
        try:
            response = requests.get(url, headers=headers, params=params, timeout=60)
            response.raise_for_status()
            data = response.json()
            items = data.get('items', [])
            
            if not items:
                break
            
            new_repos = []
            for item in items:
                full_name = item['full_name']
                
                # 去重检查
                if full_name in seen_repos:
                    continue
                
                # 停止条件：任意仓库 stars < min_stars_stop
                stars = item.get('stargazers_count', 0)
                if stars and int(stars) < min_stars_stop:
                    return all_repos
                
                seen_repos.add(full_name)
                
                new_repos.append({
                    'full_name': full_name,
                    'description': item.get('description'),
                    'stars': item.get('stargazers_count', 0),
                    'language': item.get('language'),
                    'topics': item.get('topics', []),
                    'html_url': item.get('html_url'),
                })
            
            all_repos.extend(new_repos)
            logger.info(f'分页搜索完成，已获取 {len(all_repos)} 个仓库')
            
            # 停止条件：返回结果少于 page_size（最后一页）
            if len(items) < page_size:
                break
            
            page += 1
            
        except requests.exceptions.RequestException as e:
            logger.error(f'分页搜索失败: {e}')
            return all_repos
    
    return all_repos
```

- [ ] **Step 2: Commit**

```bash
git add fetch.py
git commit -m "feat: 添加 fetch_repos_with_pagination() 支持 OR 拼接+自动翻页"
```

---

## Task 4: 重构 run_fetch() 主流程

**Files:**
- Modify: `fetch.py`

- [ ] **Step 1: 替换现有的 run_fetch() 函数为新的实现**

```python
def build_keyword_batches(keywords, max_q_length=480):
    """将关键词列表按 max_q_length 分批，每批生成 OR 拼接查询串"""
    batches = []
    
    # Step A: 构建带引号的 parts
    quoted_parts = []
    for kw in keywords:
        if ' ' in kw or '\t' in kw or '\n' in kw:
            quoted_parts.append('"' + kw + '"')
        else:
            quoted_parts.append(kw)
    
    # Step B: 贪心填充每批，直到达到 max_q_length
    current_batch = []
    current_length = 0
    
    for part, original_kw in zip(quoted_parts, keywords):
        if not current_batch:
            new_length = len(part)
        else:
            new_length = current_length + len(' OR ') + len(part)
        
        if new_length <= max_q_length:
            current_batch.append((part, original_kw))
            current_length = new_length
        else:
            batches.append(current_batch)
            current_batch = [(part, original_kw)]
            current_length = len(part)
    
    if current_batch:
        batches.append(current_batch)
    
    return batches


def run_fetch(keywords=None, top_n=None, interval=None):
    config = load_config()
    
    # 从 keywords.json 读取关键词（替代 config.json）
    kw_keys = load_keywords()
    logger.info(f'从 keywords.json 加载 {len(kw_keys)} 个关键词')
    
    max_q_length = config.get('max_q_length', 480)
    page_size = config.get('page_size', 80)
    min_stars_stop = config.get('min_stars_stop', 1000)
    
    # 分批构建查询串
    batches = build_keyword_batches(kw_keys, max_q_length)
    logger.info(f'关键词分为 {len(batches)} 批')
    
    init_db()
    
    all_repos = []
    for i, batch in enumerate(batches):
        query_parts = [item[0] for item in batch]
        original_keywords = [item[1] for item in batch]
        
        if len(batch) == 1:
            query = batch[0][0]
        else:
            query = ' OR '.join(query_parts)
        
        logger.info(f'开始抓取第 {i+1}/{len(batches)} 批，查询串长度={len(query)}')
        
        # 调用带翻页的搜索函数
        repos = fetch_repos_with_pagination(query, page_size=page_size, min_stars_stop=min_stars_stop)
        logger.info(f'第 {i+1} 批抓取完成，共 {len(repos)} 个仓库')
        
        for repo in repos:
            # keywords 字段不再更新（保留历史数据）
            repo['fetched_at'] = format_iso()
            
            readme_path = fetch_readme(repo['full_name'])
            if readme_path:
                repo['readme_path'] = readme_path
            
            upsert_repo(repo)
            all_repos.append(repo)
        
        # 批次间间隔（避免 GitHub API 限流）
        if interval and i < len(batches) - 1:
            time.sleep(interval)
    
    logger.info(f'全部抓取完成，共 {len(all_repos)} 个仓库')
    return all_repos
```

- [ ] **Step 2: Commit**

```bash
git add fetch.py
git commit -m "feat: 重构 run_fetch() 支持 OR 拼接+分页批量搜索"
```

---

## Task 5: 更新命令行参数逻辑（可选）

**Files:**
- Modify: `fetch.py`

- [ ] **Step 1: 移除 --keyword 参数的单关键词抓取逻辑**

由于现在所有关键词都从 keywords.json 读取，--keyword 参数不再适用。保留 --fetch-only 和 --translate-only 即可：

```python
if __name__ == '__main__':
    only_fetch = False
    only_translate = False
    
    if '--fetch-only' in sys.argv:
        only_fetch = True
    if '--translate-only' in sys.argv:
        only_translate = True
    
    if only_translate:
        run_translate()
    elif only_fetch:
        run_fetch()
    else:
        run_fetch()
        run_translate()
```

- [ ] **Step 2: Commit**

```bash
git add fetch.py
git commit -m "refactor: 移除 --keyword 参数，统一从 keywords.json 读取"
```

---

## Task 6: 测试验证

- [ ] **Step 1: 手动运行抓取（--fetch-only）验证流程**

```bash
python fetch.py --fetch-only
```

预期结果：
- 日志显示 "从 keywords.json 加载 X 个关键词"
- 日志显示 "关键词分为 N 批"（N=2，基于之前的估算）
- 每批查询串长度 ≤ max_q_length
- GitHub API 返回去重后的仓库列表
- README 正常保存到 data/readme/

- [ ] **Step 2: 验证数据库**

```bash
python3 -c "
import sqlite3
conn = sqlite3.connect('data/db.sqlite')
total = conn.execute('SELECT COUNT(*) FROM repositories').fetchone()[0]
print(f'数据库中总仓库数: {total}')

# 检查 keywords 字段是否仍为 NULL（新插入的记录）
null_kw = conn.execute(\"SELECT COUNT(*) FROM repositories WHERE keywords IS NULL\").fetchone()[0]
print(f'keywords 为 NULL 的记录: {null_kw}')

conn.close()
"
```

预期结果：
- total > 当前数据库中的仓库数（去重后）
- null_kw = total（新插入记录 keywords 字段为 NULL，不再更新）

---

## Task 7: 最终提交与文档更新

- [ ] **Step 1: Commit 所有变更**

```bash
git add config.py fetch.py config.json
git commit -m "feat: 重构抓取逻辑支持 OR 拼接+分页批量搜索"
```

- [ ] **Step 2: 可选 — 更新 AGENTS.md 中的常用命令部分**

将 `python fetch.py --keyword "xxx"` 改为说明关键词在 keywords.json 中配置。

---

## 影响范围总结

| 文件 | 改动类型 | 说明 |
|------|---------|------|
| `config.json` | 修改 | 新增 max_q_length/page_size/min_stars_stop |
| `config.py` | 修改 | 新增 load_keywords() |
| `fetch.py` | **核心重构** | build_search_query()/fetch_repos_with_pagination()/run_fetch() 重写 |
| `db.py` | 无改动 | keywords 字段保留不更新 |

## 风险与注意事项

1. **GitHub API 速率限制**: OR 拼接后单次查询更复杂，确保 request_interval ≥ 0.5s
2. **翻页耗时**: 如果热门仓库多（stars > 1000），可能翻页较多，注意超时时间设为 60s
3. **去重逻辑**: seen_repos 集合在内存中维护，若结果集极大需考虑分批写入数据库
