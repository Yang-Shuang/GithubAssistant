# 翻译排序优化与清理脚本设计

> 日期: 2026-06-04
> 状态: 已批准

## 需求概述

两个独立功能：
1. **翻译按星标排序** — README和描述翻译队列改为按 stars DESC 排列，热门内容优先处理
2. **清理脚本 clear.py** — 清理低星标仓库数据（stars < limit），默认预览模式，需 --execute 才执行删除

## 设计详情

### 功能一：翻译按星标排序

**修改文件：** `db.py:get_pending_translates()`、`translator.py:run_translate_descriptions()`
**改动内容：** SQL 查询从 `ORDER BY id ASC` 改为 `ORDER BY stars DESC`

### 功能二：清理脚本 clear.py

**新建文件：** `clear.py`
**配置字段：** config.json 新增 `"clear_limit_count": 2000`

**安全设计：**
- 默认预览模式（只查询，不删除）
- 需显式传入 `--execute` 才执行删除操作
- 删除前输出统计信息：记录数、文件列表

## 影响范围

| 文件 | 变更类型 | 说明 |
|------|---------|------|
| db.py:219-224 | 修改SQL | get_pending_translates() ORDER BY stars DESC |
| translator.py:253 | 修改SQL | run_translate_descriptions() ORDER BY stars DESC |
| config.json | 新增字段 | clear_limit_count = 2000 |
| clear.py | **新建** | 清理脚本（预览+执行模式） |

## 风险评估

- **翻译排序：** 低风险，仅改变查询顺序，不影响数据完整性
- **清理脚本：** 中风险，涉及数据删除。通过默认预览模式 + --execute 标志降低风险
