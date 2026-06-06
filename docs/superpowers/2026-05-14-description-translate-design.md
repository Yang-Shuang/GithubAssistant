# 描述信息中文翻译设计文档

## 概述

在仓库列表页展示描述信息的中文翻译，支持批量翻译所有未翻译的描述，可随时中断。

## 数据库变更

### repositories 表新增字段

```sql
ALTER TABLE repositories ADD COLUMN description_zh TEXT;
ALTER TABLE repositories ADD COLUMN description_translate_status TEXT DEFAULT 'pending';
```

- `description_zh` — 中文描述译文
- `description_translate_status` — 翻译状态（`pending` / `translating` / `done` / `failed`），与现有 `translate_status` 字段并行，避免混淆 README 翻译和描述翻译

### 已有函数变更

| 函数 | 变更内容 |
|------|---------|
| `upsert_repo()` | 新增 `description_zh`、`description_translate_status` 参数，ON CONFLICT 时不更新这两个字段 |
| `get_repos()` | 返回结果包含新字段 |
| `get_repo()` | 返回结果包含新字段 |

## API 变更

### 已有接口变更

| Method | Path | 变更 |
|--------|------|------|
| GET | `/api/repos` | 返回结果中新增 `description_zh`、`description_translate_status` 字段 |

### 新增接口

| Method | Path | 说明 |
|--------|------|------|
| POST | `/api/description/translate` | 触发批量翻译（异步线程） |
| GET | `/api/description/translate/status` | 查询进度（running / stopped / done） |
| POST | `/api/description/translate/stop` | 设置中断标志 |

## 后端实现

### translator.py 新增函数

```python
description_translate_stop = False  # 全局中断标志
```

**`translate_description(description)`**
- 复用 `call_llm()`，传入 `TRANSLATE_PROMPT.format(content=description)`
- 与 `translate_readme()` 使用相同的翻译规则（产品名、命令等不翻译）

**`translate_description_single(repo_id)`**
- 读取 `repositories` 中 `description` 字段
- 调用 `translate_description()` 翻译
- 更新数据库：`description_zh`、`description_translate_status='done'`
- 返回是否成功

**`run_translate_descriptions()`**
- 查询 `description_translate_status='pending' AND description IS NOT NULL AND description != ''` 的记录
- 按 `id ASC` 顺序逐条翻译
- 每翻译一条检查 `description_translate_stop` 标志，如果为 True 则跳出循环
- 返回统计信息（总数、成功数、失败数、是否被中断）

### server.py 新增路由

**`POST /api/description/translate`**
- 设置 `description_translate_stop = False`
- 启动线程执行 `run_translate_descriptions()`
- 返回 `{'status': 'started'}`

**`GET /api/description/translate/status`**
- 返回 `{'running': bool, 'total': int, 'done': int, 'failed': int, 'stopped': bool}`

**`POST /api/description/translate/stop`**
- 设置 `description_translate_stop = True`
- 返回 `{'status': 'stopped'}`

## 前端实现

### index.html 变更

在 `.stats-bar` 中新增：
- "翻译全部"按钮（`#translate-desc-btn`）
- "停止"按钮（`#stop-translate-btn`，默认隐藏）
- 进度展示区域（`#desc-translate-progress`）

### index.html 列表项渲染变更

```html
<div class="repo-desc">${repo.description || '暂无描述'}</div>
${repo.description_zh ? `<div class="repo-desc-zh">${repo.description_zh}</div>` : ''}
```

### app.js 新增函数

**`startTranslateDescriptions()`**
- 禁用"翻译全部"按钮，启用"停止"按钮
- POST `/api/description/translate`
- 开始轮询

**`pollDescriptionTranslateStatus()`**
- 每 2 秒 GET `/api/description/translate/status`
- 更新进度条显示（已翻译/总数）
- 如果 `stopped` 或 `done`，停止轮询，重置按钮状态
- 翻译完成后刷新列表

### style.css 新增样式

```css
.repo-desc-zh {
    color: #888;
    font-size: 12px;
    margin-top: 2px;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
}
```

## 数据流

```
用户点击"翻译全部"
  → POST /api/description/translate
  → 后端启动线程，遍历 pending 记录
  → 前端轮询 GET /api/description/translate/status
  → 每翻译一条，数据库更新 description_zh + description_translate_status='done'
  → 前端轮询到 done/stopped，停止轮询，刷新列表
```

## 错误处理

- 单条翻译失败：`description_translate_status='failed'`，记录 `translate_error`（复用现有字段），继续翻译下一条
- API 调用失败：重试 3 次，指数退避（复用 `call_llm()` 现有逻辑）
- 中断后：已翻译的保留，未翻译的保持 `pending`，下次可重新触发

## 影响范围

| 文件 | 变更类型 |
|------|---------|
| `db.py` | 新增字段适配 |
| `server.py` | 新增 3 个路由 |
| `translator.py` | 新增 3 个函数 + 全局标志 |
| `index.html` | 新增按钮和进度区域 |
| `app.js` | 新增 2 个函数，修改列表渲染 |
| `style.css` | 新增 `.repo-desc-zh` 样式 |
