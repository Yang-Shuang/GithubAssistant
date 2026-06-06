# Translate Sort & Clear Script Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use subagent-driven-development (recommended) or executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 翻译队列按星标排序 + 新增安全的清理脚本
**Architecture:** 修改两处SQL查询实现排序优化；新建clear.py使用预览模式+--execute标志确保数据安全
**Tech Stack:** Python, sqlite3, argparse, config.json

---

### Task 1: 修改 db.py - get_pending_translates() 按 stars DESC 排序

**Files:**
- Modify: `db.py:219-224`

- [ ] **Step 1: 查看当前代码上下文**

```bash
nl -ba /mnt/e/Projects/htmlSpace/GithubAssistant/db.py | sed -n '219,235p'
```

预期输出应显示：
```python
def get_pending_translates(limit=10):
    conn = get_connection()
    cursor = conn.execute(
        'SELECT * FROM repositories WHERE translate_status = ? ORDER BY id ASC LIMIT ?',
        ('pending', limit)
    )
```

- [ ] **Step 2: 修改 SQL 查询**

将 `ORDER BY id ASC` 改为 `ORDER BY stars DESC NULLS LAST`：

```python
# db.py:221-223
cursor = conn.execute(
    'SELECT * FROM repositories WHERE translate_status = ? ORDER BY stars DESC NULLS LAST LIMIT ?',
    ('pending', limit)
)
```

**说明：** `NULLS LAST` 确保没有stars值的记录排在最后（GitHub API偶尔返回空值）

- [ ] **Step 3: 验证语法正确性**

```bash
python -c "import ast; ast.parse(open('db.py').read()); print('Syntax OK')"
```

预期输出：`Syntax OK`

---

### Task 2: 修改 translator.py - run_translate_descriptions() 按 stars DESC 排序

**Files:**
- Modify: `translator.py:253`

- [ ] **Step 1: 查看当前代码上下文**

```bash
nl -ba /mnt/e/Projects/htmlSpace/GithubAssistant/translator.py | sed -n '249,260p'
```

预期输出应显示：
```python
cursor = conn.execute(
    'SELECT * FROM repositories WHERE description_translate_status = ? AND description IS NOT NULL AND LENGTH(description) > 0 ORDER BY id ASC',
    ('pending',)
)
```

- [ ] **Step 2: 修改 SQL 查询**

将 `ORDER BY id ASC` 改为 `ORDER BY stars DESC NULLS LAST`：

```python
# translator.py:253
cursor = conn.execute(
    'SELECT * FROM repositories WHERE description_translate_status = ? AND description IS NOT NULL AND LENGTH(description) > 0 ORDER BY stars DESC NULLS LAST',
    ('pending',)
)
```

- [ ] **Step 3: 验证语法正确性**

```bash
python -c "import ast; ast.parse(open('translator.py').read()); print('Syntax OK')"
```

预期输出：`Syntax OK`

---

### Task 3: config.json 新增 clear_limit_count 字段

**Files:**
- Modify: `config.json`

- [ ] **Step 1: 查看当前配置结构**

```bash
cat /mnt/e/Projects/htmlSpace/GithubAssistant/config.json
```

- [ ] **Step 2: 在 config.json 末尾添加 clear_limit_count**

使用 jq 或直接编辑：

```json
{
  "github_token": "...",
  ...其他字段...,
  "clear_limit_count": 2000,
  "update_all": false
}
```

实际命令（追加到最后一个对象键之前）：
```bash
python -c "
import json
with open('config.json', 'r') as f:
    data = json.load(f)
data['clear_limit_count'] = 2000
with open('config.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print('Updated config.json')
"
```

- [ ] **Step 3: 验证 JSON 格式**

```bash
python -c "import json; json.load(open('config.json')); print('JSON valid')"
```

预期输出：`JSON valid`

---

### Task 4: 新建 clear.py 清理脚本

**Files:**
- Create: `clear.py`

- [ ] **Step 1: 创建文件并写入完整代码**

```python
"""
clear.py - GitHub Reader 数据清理工具

用法：
    python clear.py              # 预览模式（默认）
    python clear.py --execute    # 执行删除操作

安全设计：
- 默认只查询不删除，显示即将操作的记录列表
- 需要显式传入 --execute 才真正执行删除
"""

import sys
import os
from config import load_config, get_db_path, get_readme_dir
from utils import setup_logger, repo_to_filename, repo_to_filename_zh

logger = setup_logger('clear')


def query_low_stars_repos(min_stars=1000):
    """查询 stars < min_stars 的仓库记录"""
    import sqlite3
    
    db_path = get_db_path()
    conn = sqlite3.connect(db_path)
    cursor = conn.execute(
        '''SELECT id, full_name, description, stars, language 
           FROM repositories 
           WHERE stars < ? OR stars IS NULL
           ORDER BY stars ASC''',
        (min_stars,)
    )
    
    repos = []
    for row in cursor:
        repo_id, full_name, desc, stars, lang = row
        # 检查 readme 文件是否存在
        readme_dir = get_readme_dir()
        
        # 查找 .md 和 _zh.md 文件
        md_files = []
        try:
            for fname in os.listdir(readme_dir):
                if full_name.replace('/', '_') in fname and fname.endswith('.md'):
                    md_files.append(os.path.join(readme_dir, fname))
        except Exception as e:
            logger.warning(f'扫描 readme 目录失败: {e}')
        
        repos.append({
            'id': repo_id,
            'full_name': full_name,
            'stars': stars or 0,
            'description_zh_path': os.path.join(readme_dir, repo_to_filename_zh(full_name)) if stars else None,
            'readme_files': md_files,
        })
    
    conn.close()
    return repos


def delete_repos(repos):
    """删除仓库记录和相关文件"""
    import sqlite3
    
    db_path = get_db_path()
    readme_dir = get_readme_dir()
    
    for repo in repos:
        full_name = repo['full_name']
        
        # 删除数据库记录
        conn = sqlite3.connect(db_path)
        conn.execute('DELETE FROM repositories WHERE id = ?', (repo['id'],))
        conn.commit()
        conn.close()
        logger.info(f'已删除: {full_name} (stars={repo["stars"]})')
        
        # 删除 readme 文件
        for md_file in repo.get('readme_files', []):
            if os.path.exists(md_file):
                os.remove(md_file)
                logger.info(f'已删除文件: {md_file}')


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='GitHub Reader 数据清理工具')
    parser.add_argument(
        '--execute', 
        action='store_true', 
        help='执行删除操作（默认只预览）'
    )
    
    args = parser.parse_args()
    
    # 加载配置
    config = load_config()
    clear_limit_count = config.get('clear_limit_count', 2000)
    
    logger.info(f'清理阈值: stars < {clear_limit_count}')
    
    if not args.execute:
        print('=' * 60)
        print('预览模式 - 即将删除以下记录:')
        print('=' * 60)
        
        repos = query_low_stars_repos(clear_limit_count)
        
        if not repos:
            print('没有需要清理的记录')
            return
        
        total_files = sum(len(r.get('readme_files', [])) for r in repos)
        
        print(f'\n总计: {len(repos)} 条记录, {total_files} 个文件\n')
        print('-' * 60)
        
        for repo in repos[:20]:  # 只打印前20条预览
            stars_str = str(repo['stars']) if repo['stars'] else 'N/A'
            files_info = f', {len(repo.get("readme_files", []))} 个文件' if repo.get('readme_files') else ''
            print(f'{repo["full_name"]} (stars={stars_str}){files_info}')
        
        if len(repos) > 20:
            print(f'... 还有 {len(repos) - 20} 条记录未显示\n')
        
        print('=' * 60)
        print('确认无误后，运行 python clear.py --execute 执行删除操作')
        print('=' * 60)
    else:
        print('=' * 60)
        print('执行模式 - 正在删除数据...')
        print('=' * 60)
        
        repos = query_low_stars_repos(clear_limit_count)
        
        if not repos:
            print('没有需要清理的记录')
            return
        
        total_files = sum(len(r.get('readme_files', [])) for r in repos)
        
        print(f'总计: {len(repos)} 条记录, {total_files} 个文件')
        
        # 二次确认
        confirm = input('\n确定要删除这些记录吗？(yes/no): ')
        if confirm.lower() != 'yes':
            print('操作已取消')
            return
        
        delete_repos(repos)
        
        print(f'\n清理完成: {len(repos)} 条记录, {total_files} 个文件')


if __name__ == '__main__':
    main()
```

- [ ] **Step 2: 验证语法正确性**

```bash
python -c "import ast; ast.parse(open('clear.py').read()); print('Syntax OK')"
```

预期输出：`Syntax OK`

---

### Task 5: 测试验证

- [ ] **Step 1: 运行预览模式（不执行删除）**

```bash
cd /mnt/e/Projects/htmlSpace/GithubAssistant && python clear.py
```

**安全测试：** 确认只打印列表，没有删除任何数据或文件。

预期输出应显示：
- `清理阈值: stars < 2000`
- 仓库列表（full_name, stars）
- `确认无误后，运行 python clear.py --execute 执行删除操作`

- [ ] **Step 2: 验证翻译排序查询**

```bash
cd /mnt/e/Projects/htmlSpace/GithubAssistant && python -c "
from db import get_connection
conn = get_connection()
cursor = conn.execute(
    'SELECT id, full_name, stars FROM repositories WHERE translate_status = ? ORDER BY stars DESC NULLS LAST LIMIT 5',
    ('pending',)
)
for row in cursor:
    print(f'{row[1]} (stars={row[2]})')
conn.close()
"
```

预期输出：显示 stars 最高的5个待翻译仓库（按星星数降序）

- [ ] **Step 3: 验证 config.json**

```bash
python -c "from config import load_config; print(load_config()['clear_limit_count'])"
```

预期输出：`2000`

---

### Task 6: Git 提交

- [ ] **Step 1: 暂存所有更改**

```bash
git add db.py translator.py config.json clear.py docs/superpowers/specs/2026-06-04-translate-sort-and-clear-design.md
```

- [ ] **Step 2: 提交变更**

```bash
git commit -m "feat: 翻译按星标排序 + 新增清理脚本"
```

---

## Self-Review Checklist

1. ✅ **Spec coverage:** 设计文档中所有6个条目都有对应任务（Task 1-4）
2. ✅ **Placeholder scan:** 无"TBD"/"TODO"等占位符，所有代码完整呈现
3. ✅ **Type consistency:** config.json 字段名 `clear_limit_count` 在 clear.py 和 Task 5 Step 3 中保持一致
4. ✅ **Scope check:** 仅修改翻译排序 + 新增清理脚本，无多余功能

## Risk Assessment

- **低：** db.py/translator.py SQL 修改仅改变排序顺序，不影响数据完整性
- **中：** clear.py 涉及删除操作，但通过预览模式+二次确认降低风险
