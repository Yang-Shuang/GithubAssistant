# GitHub 抓取逻辑重构设计

## 背景

当前项目每次抓取时对 `config.json` 中的每个关键词单独调用一次 GitHub Search API，导致：
- 大量重复数据（如 "agent"、"ai agent"、"developer agent" 搜索同一仓库）
- API 调用次数多，容易触发速率限制
- keywords 字段记录不准确

## 目标

将抓取逻辑改为 **OR 拼接批量搜索**，减少重复数据、优化 API 调用效率。

## 核心设计

### 1. 关键词读取

从 `keywords.json` 中读取所有 `key` 值（不包含 description）。

```json
{
    "keywords": [
        {"key": "vibe coding", "description": "..."},
        {"key": "ai agent", "description": "..."}
    ]
}
```

提取逻辑：`[kw["key"] for kw in data["keywords"]]`

### 2. OR 拼接构建 q 参数

- **含空格的关键词**必须加双引号，如 `"vibe coding"`
- **不含空格的关键词**不加引号，如 `agent`
- 用 ` OR `（大写）连接
- **总长度限制**：最长不超过可配置值（默认 480 字符），超长则截断

拼接示例：
```python
keywords = ["vibe coding", "ai agent", "agent"]
# → '"vibe coding" OR "ai agent" OR agent'
```

### 3. GitHub Search API 调用参数

| 参数 | 值 | 说明 |
|------|-----|------|
| `q` | OR 拼接后的关键词串 | 最长可配置（默认480） |
| `sort` | `stars` | 按星标数降序 |
| `order` | `desc` | 降序排列 |
| `per_page` | 80 | 每页最大数量，可配置（官方上限100） |

### 4. 翻页逻辑

- **起始**：page=1
- **判断停止条件**（任一满足即停）：
  1. 当前页返回结果中 **任意一个仓库** 的 `stargazers_count < min_stars_stop`（默认1000，可配置）
  2. 当前页返回的结果数量 `< per_page`（最后一页）
- **合并去重**：GitHub API 自动处理同一仓库不会重复出现

### 5. keywords 字段行为

- `keywords` 字段保留在数据库中
- **不再更新该字段**，保持历史数据不变
- 后续前端标签展示改用 `topics` 字段（来自 GitHub topics）

## 配置文件变更

### config.json 新增项

```json
{
    "max_q_length": 480,
    "page_size": 80,
    "min_stars_stop": 1000
}
```

### keywords.json 结构不变

保留现有格式，description 字段继续用于用户查看。

## 代码变更范围

| 文件 | 改动内容 |
|------|---------|
| `config.py` | 新增路径获取函数（如需） |
| `fetch.py` | **核心改动**：重构抓取逻辑 |
| `db.py` | 无改动（keywords 字段保留不更新） |

## 影响范围

- ✅ **减少重复数据**：同一仓库不会因多个关键词被多次保存
- ✅ **优化 API 调用**：从 N 次/关键词 → 1~2 次（OR拼接+翻页）
- ⚠️ **keywords 字段不再更新**：历史数据保留，新数据 keywords 为空或旧值
