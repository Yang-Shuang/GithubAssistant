# GitHub Reader 公开模块设计文档

> 日期: 2026-06-04
> 状态: 已批准

## 需求概述

创建一个纯静态的GitHub Pages展示模块，用于公开浏览抓取到的仓库信息。该模块不包含后端代码、无信息抓取能力、SQLite数据库只读。用户本地完成抓取和翻译后，手动导出数据到public目录并提交推送。

## 设计详情

### 1. 项目结构

```
public/                          # GitHub Pages部署根目录（独立git仓库）
├── index.html                   # 列表页（/?page=1&sort_by=fetched_at&sort_order=desc）
├── detail.html                  # 详情页（/?id=123或/detail.html?id=123）
├── style.css                    # 统一响应式样式
├── app.js                       # 前端逻辑：JSON加载、渲染、排序
├── export.py                    # Python导出脚本（本地运行，从SQLite读取数据）
├── .gitignore                   # 忽略data/目录
└── data/                        # 生成的静态文件（不提交到Git）
    ├── repos.json               # 仓库数据JSON
    └── readmes/                 # README副本
        ├── owner__repo.md
        └── owner__repo_zh.md
```

### 2. 列表页设计（紧凑风格方案C）

**布局结构：**
- 顶部导航栏：简洁标题 + GitHub Logo
- 排序按钮组：三种排序方式（最新抓取、最早抓取、最多星标），固定在右侧
- 列表项：GitHub风格的行内列表，三列信息（名称|描述|stars）
- 分页组件：底部居中显示

**关键特性：**
- **移动端优先**：单列大间距布局，点击整行跳转详情
- **PC端增强**：紧凑多列展示，hover效果提升交互体验
- **数据密度高**：每屏80条记录（config.json配置）
- **URL参数传递排序状态**

### 3. 详情页设计

**布局结构：**
- 顶部导航栏：返回按钮 + 仓库名称
- 信息卡片区：Description、Stars、Language、GitHub链接
- README切换Tab：中文/English即时切换，URL带`?lang=zh`参数
- Markdown内容区：沉浸式阅读体验

**关键特性：**
- **移动端**：上下单栏布局，README切换按钮固定在顶部
- **PC端双栏**：左侧信息卡片（280px固定）+ 右侧Markdown内容区（自适应宽度）
- **按需加载**：README文件仅在点击详情页时fetch，避免首屏阻塞

### 4. Python导出脚本 (export.py)

```python
# export.py - 从本地SQLite导出为JSON + README文件
import sqlite3, json, os, shutil
from config import get_db_path, get_readme_dir

def export():
    conn = sqlite3.connect(get_db_path())
    
    # 查询所有仓库数据（排除is_read状态）
    repos = conn.execute('''
        SELECT id, full_name, description, stars, language, 
               topics, html_url, readme_path, readme_zh_path, 
               fetched_at 
        FROM repositories 
        ORDER BY id DESC
    ''').fetchall()
    
    output_data = []
    for row in repos:
        # 转换topics为JSON数组，过滤空值
        repo_dict = dict(row)
        if isinstance(repo_dict.get('topics'), str):
            repo_dict['topics'] = json.loads(repo_dict['topics'])
        
        # 添加相对路径用于前端引用
        readme_src = get_readme_dir()
        if repo_dict.get('readme_path'):
            repo_dict['relative_readme_path'] = os.path.relpath(
                repo_dict['readme_path'], readme_src)
        if repo_dict.get('readme_zh_path'):
            repo_dict['relative_readme_zh_path'] = os.path.relpath(
                repo_dict['readme_zh_path'], readme_src)
        
        output_data.append(repo_dict)
    
    # 写入repos.json（压缩格式）
    with open('data/repos.json', 'w') as f:
        json.dump(output_data, f, ensure_ascii=False, separators=(',', ':'))
    
    # 复制README文件到public/data/readmes/
    readme_dst = 'data/readmes'
    os.makedirs(readme_dst, exist_ok=True)
    
    for repo in output_data:
        if repo.get('readme_path'):
            src_file = repo['readme_path']
            dst_file = f"{repo['full_name'].replace('/', '_')}.md"
            shutil.copy2(src_file, os.path.join(readme_dst, dst_file))
        
        if repo.get('readme_zh_path'):
            src_file = repo['readme_zh_path']
            dst_file = f"{repo['full_name'].replace('/', '_')}_zh.md"
            shutil.copy2(src_file, os.path.join(readme_dst, dst_file))

if __name__ == '__main__':
    export()
```

### 5. 数据流设计

```
本地项目 → python3 export.py → repos.json + readmes/ → git push → GitHub Pages
                                    ↓
                              浏览器 fetch('data/repos.json')
                                    ↓
                          app.js加载JSON渲染列表页
                                    ↓
                          点击列表项 → detail.html?id=X
                                    ↓
                          fetch(`data/readmes/${filename}.md`)
```

**性能考虑：**
- `repos.json` 压缩后约50KB（gzip）
- README按需懒加载（仅当前详情页请求一次）
- 分页：每页20条记录，前端处理分页逻辑

### 6. UI设计细节

**配色方案：**
- 主色：GitHub原生蓝色 `#0366d6` + 浅灰背景 `#f8f9fa`
- 强调色：星标金色 `#f0c000`、成功绿 `#28a745`

**字体栈：** 
```css
font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
```

**响应式断点：**
```css
/* 移动端（≤768px） */
@media (max-width: 768px) { /* 单列大间距布局 */ }

/* PC端（>769px） */
@media (min-width: 769px) { /* 紧凑多列/双栏布局 */ }
```

**Markdown渲染：** 
- 使用CDN引入marked.js + DOMPurify
- 自定义样式：代码块背景`#f6f8fa`、表格边框`#dee2e6`

### 7. 文件变更清单

| 文件 | 操作 | 说明 |
|------|------|------|
| `public/index.html` | **新建** | 列表页HTML结构（URL参数支持排序/分页） |
| `public/detail.html` | **新建** | 详情页HTML结构（README语言切换Tab） |
| `public/style.css` | **新建** | 响应式样式（移动端优先，双栏PC布局） |
| `public/app.js` | **新建** | JSON加载、渲染、排序逻辑、分页组件 |
| `public/export.py` | **新建** | Python导出脚本（SQLite→JSON+README文件） |

### 8. 风险评估

- **低风险：** 纯静态页面，无后端依赖，GitHub Pages原生支持
- **中风险：** README文件体积较大时影响首屏加载 → 通过按需懒加载解决
- **低维护成本：** 数据由Python脚本预生成，无需数据库服务或API调用
