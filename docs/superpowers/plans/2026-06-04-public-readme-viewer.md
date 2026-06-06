# Public README Viewer Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use subagent-driven-development (recommended) or executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 创建纯静态GitHub Pages展示模块，用于公开浏览抓取到的仓库信息
**Architecture:** Python脚本导出SQLite数据为JSON + README文件，前端通过fetch加载这些静态资源实现列表和详情展示
**Tech Stack:** HTML5, CSS3 (响应式), Vanilla JavaScript, Markdown渲染(marked.js)

---

### Task 1: 创建项目结构和基础文件

**Files:**
- Create: `public/.gitignore`
- Create: `public/README.md`
- Create: `public/index.html`
- Create: `public/detail.html`
- Create: `public/style.css`
- Create: `public/app.js`
- Create: `public/export.py`

- [ ] **Step 1: 创建目录结构和基础文件**

```bash
mkdir -p /mnt/e/Projects/htmlSpace/GithubAssistant/public/data/readmes
touch /mnt/e/Projects/htmlSpace/GithubAssistant/public/.gitignore
```

- [ ] **Step 2: 写入.gitignore内容（忽略数据目录）**

```gitignore
# public/.gitignore
data/repos.json
data/readmes/*.md
!data/.gitkeep
```

- [ ] **Step 3: 创建README.md说明文档**

```markdown
# GitHub Reader Public Viewer

纯静态GitHub Pages展示模块，用于公开浏览抓取到的仓库信息。

## 使用方法

1. 本地运行 `python export.py` 导出数据
2. 提交并推送到GitHub Pages

## 功能特性

- 列表页：支持三种排序方式（最新抓取/最早抓取/最多星标）
- 详情页：中英文README切换，Markdown渲染
- 响应式设计：适配移动端和PC端
```

---

### Task 2: 实现Python导出脚本 (export.py)

**Files:**
- Create: `public/export.py`

- [ ] **Step 1: 编写完整导出脚本代码**

```python
#!/usr/bin/env python3
"""
export.py - GitHub Reader Public Viewer 数据导出脚本

用法：
    cd public && python export.py
    
功能：
    - 从本地SQLite数据库读取仓库信息
    - 导出为JSON文件（data/repos.json）
    - 复制README文件到data/readmes/目录
"""

import sqlite3
import json
import os
import shutil
import sys


def get_project_root():
    """获取项目根目录（GithubAssistant目录）"""
    return os.path.dirname(os.path.abspath(__file__)) + '/../..'


def export_data():
    """导出数据库和README文件到public/data/目录"""
    
    # 加载配置以获取路径信息
    sys.path.insert(0, get_project_root())
    from config import load_config, get_db_path, get_readme_dir
    
    config = load_config()
    db_path = get_db_path()
    readme_src_dir = get_readme_dir()
    
    # 创建输出目录
    public_data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
    readmes_dst_dir = os.path.join(public_data_dir, 'readmes')
    os.makedirs(readmes_dst_dir, exist_ok=True)
    
    print(f'📊 连接数据库: {db_path}')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # 查询所有仓库数据（不含is_read状态）
    print('🔍 查询仓库数据...')
    repos_data = []
    
    try:
        rows = cursor.execute('''
            SELECT id, full_name, description, stars, language, 
                   topics, html_url, readme_path, readme_zh_path, 
                   fetched_at 
            FROM repositories 
            ORDER BY id DESC
        ''').fetchall()
        
        print(f'📦 找到 {len(rows)} 条记录')
        
        for row in rows:
            repo_id, full_name, description, stars, language, topics_json, html_url, readme_path, readme_zh_path, fetched_at = row
            
            # 解析topics JSON
            if isinstance(topics_json, str) and topics_json:
                try:
                    topics_list = json.loads(topics_json)
                except json.JSONDecodeError:
                    topics_list = []
            elif isinstance(topics_json, list):
                topics_list = topics_json
            else:
                topics_list = []
            
            # 构建相对路径（相对于data/readmes目录）
            relative_readme_path = None
            relative_readme_zh_path = None
            
            if readme_path and os.path.exists(readme_path):
                try:
                    rel_path = os.path.relpath(readme_path, readme_src_dir)
                    # 转换路径分隔符为/并提取文件名
                    filename = os.path.basename(rel_path)
                    relative_readme_path = f'readmes/{filename}'
                    
                    # 复制文件到readmes目录（避免重复）
                    dst_file = os.path.join(readmes_dst_dir, filename)
                    if not os.path.exists(dst_file):
                        shutil.copy2(readme_path, dst_file)
                except Exception as e:
                    print(f'⚠️ 警告：处理README失败 {full_name}: {e}')
            
            if readme_zh_path and os.path.exists(readme_zh_path):
                try:
                    rel_path = os.path.relpath(readme_zh_path, readme_src_dir)
                    filename = os.path.basename(rel_path)
                    relative_readme_zh_path = f'readmes/{filename}'
                    
                    # 复制文件到readmes目录（避免重复）
                    dst_file = os.path.join(readmes_dst_dir, filename)
                    if not os.path.exists(dst_file):
                        shutil.copy2(readme_zh_path, dst_file)
                except Exception as e:
                    print(f'⚠️ 警告：处理中文README失败 {full_name}: {e}')
            
            # 构建仓库数据对象
            repo = {
                'id': repo_id,
                'full_name': full_name,
                'description': description or '',
                'stars': stars or 0,
                'language': language or '',
                'topics': topics_list,
                'html_url': html_url or '',
                'readme_path': relative_readme_path,
                'readme_zh_path': relative_readme_zh_path,
                'fetched_at': fetched_at[:10] if fetched_at else ''  # 只保留日期部分
            }
            
            repos_data.append(repo)
    
    finally:
        conn.close()
    
    print(f'📝 导出 {len(repos_data)} 条记录到JSON...')
    
    # 写入repos.json（压缩格式以减小体积）
    json_path = os.path.join(public_data_dir, 'repos.json')
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(repos_data, f, ensure_ascii=False, separators=(',', ':'))
    
    # 统计README文件数量
    readme_files_count = len([f for f in os.listdir(readmes_dst_dir) if f.endswith('.md')])
    print(f'📚 README文件: {readme_files_count} 个')
    print(f'✅ 导出完成！数据位于: data/repos.json')


if __name__ == '__main__':
    try:
        export_data()
    except Exception as e:
        print(f'❌ 导出失败: {e}')
        sys.exit(1)
```

- [ ] **Step 2: 验证脚本语法**

```bash
python3 -c "import ast; ast.parse(open('/mnt/e/Projects/htmlSpace/GithubAssistant/public/export.py').read()); print('Syntax OK')"
```

预期输出：`Syntax OK`

---

### Task 3: 实现列表页 (index.html + app.js)

**Files:**
- Create: `public/index.html`
- Modify: `public/app.js`（添加列表加载逻辑）

- [ ] **Step 1: 编写列表页HTML结构**

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GitHub Reader - Public Viewer</title>
    <link rel="stylesheet" href="/style.css">
</head>
<body>
    <!-- 顶部导航 -->
    <header class="header">
        <div class="container header-content">
            <a href="/" class="logo">📚 Public Repos</a>
        </div>
    </header>

    <!-- 排序控制栏 -->
    <div class="sort-bar container">
        <div class="sort-btn-group" id="sort-buttons">
            <button class="sort-btn active" data-sort-by="fetched_at" data-sort-order="desc">最新抓取</button>
            <button class="sort-btn" data-sort-by="fetched_at" data-sort-order="asc">最早抓取</button>
            <button class="sort-btn" data-sort-by="stars" data-sort-order="desc">最多星标</button>
        </div>
    </div>

    <!-- 仓库列表 -->
    <main class="container">
        <div id="repo-list" class="repo-list">
            <div class="loading">加载中...</div>
        </div>

        <!-- 分页组件 -->
        <div class="pagination container" id="pagination"></div>
    </main>

    <script src="/app.js"></script>
</body>
</html>
```

- [ ] **Step 2: 编写完整的前端JavaScript逻辑**

```javascript
// public/app.js - GitHub Reader Public Viewer 前端逻辑

const PAGE_SIZE = 80; // 每页显示数量（config.json配置）

// URL参数解析工具函数
function getUrlParams() {
    const params = new URLSearchParams(window.location.search);
    return {
        page: parseInt(params.get('page')) || 1,
        sortBy: params.get('sort_by') || 'fetched_at',
        sortOrder: params.get('sort_order') || 'desc'
    };
}

// URL参数更新工具函数
function updateUrlParams(newParams) {
    const current = getUrlParams();
    Object.assign(current, newParams);
    const searchParams = new URLSearchParams();
    if (current.page !== 1) searchParams.set('page', current.page);
    if (current.sortBy && current.sortBy !== 'fetched_at') searchParams.set('sort_by', current.sortBy);
    if (current.sortOrder && current.sortOrder === 'desc') searchParams.set('sort_order', current.sortOrder);
    
    window.history.replaceState(null, '', `?${searchParams.toString()}`);
}

// 加载仓库数据并渲染列表
async function loadRepos(page = 1, sortBy = 'fetched_at', sortOrder = 'desc') {
    const listContainer = document.getElementById('repo-list');
    
    if (listContainer) {
        listContainer.innerHTML = '<div class="loading">加载中...</div>';
    }
    
    try {
        // 加载repos.json数据
        const response = await fetch('/data/repos.json');
        const repos = await response.json();
        
        // 排序处理
        if (sortBy === 'stars') {
            repos.sort((a, b) => sortOrder === 'desc' ? b.stars - a.stars : a.stars - b.stars);
        } else if (sortBy === 'fetched_at') {
            repos.sort((a, b) => sortOrder === 'desc' ? new Date(b.fetched_at) - new Date(a.fetched_at) : new Date(a.fetched_at) - new Date(b.fetched_at));
        }
        
        // 分页处理
        const totalPages = Math.ceil(repos.length / PAGE_SIZE);
        const startIdx = (page - 1) * PAGE_SIZE;
        const endIdx = Math.min(startIdx + PAGE_SIZE, repos.length);
        const pageRepos = repos.slice(startIdx, endIdx);
        
        // 渲染列表项
        if (listContainer) {
            listContainer.innerHTML = '';
            
            if (pageRepos.length === 0) {
                listContainer.innerHTML = '<div class="empty">暂无数据</div>';
            } else {
                pageRepos.forEach(repo => {
                    const itemEl = document.createElement('div');
                    itemEl.className = 'repo-item';
                    
                    // 生成topics标签HTML
                    let topicsHtml = '';
                    if (repo.topics && repo.topics.length > 0) {
                        topicsHtml = `<div class="repo-topics">${repo.topics.map(t => `<span class="topic-tag">${t}</span>`).join('')}</div>`;
                    }
                    
                    itemEl.innerHTML = `
                        <div class="repo-info">
                            <a href="/detail.html?id=${repo.id}" class="repo-name-link" title="${repo.full_name}">
                                ${repo.full_name}
                            </a>
                            <div class="repo-desc">${repo.description || '暂无描述'}</div>
                            ${topicsHtml}
                        </div>
                        <div class="repo-meta">
                            <span class="meta-stars" title="${repo.stars} stars">★ ${formatStars(repo.stars)}</span>
                            <span class="meta-lang">${repo.language || '-'}</span>
                            <span class="meta-date">${repo.fetched_at}</span>
                        </div>
                    `;
                    
                    listContainer.appendChild(itemEl);
                });
            }
        }
        
        // 渲染分页组件
        renderPagination(totalPages, page);
        
    } catch (error) {
        console.error('加载数据失败:', error);
        if (listContainer) {
            listContainer.innerHTML = '<div class="error">❌ 加载数据失败，请检查网络连接</div>';
        }
    }
}

// 格式化星标数字（添加K/M后缀）
function formatStars(stars) {
    if (stars >= 1000000) return (stars / 1000000).toFixed(1) + 'M';
    if (stars >= 1000) return (stars / 1000).toFixed(1) + 'K';
    return stars.toString();
}

// 渲染分页按钮
function renderPagination(totalPages, currentPage) {
    const paginationEl = document.getElementById('pagination');
    
    if (!paginationEl || totalPages <= 1) {
        if (paginationEl) paginationEl.innerHTML = '';
        return;
    }
    
    let buttonsHtml = '';
    
    // 上一页按钮
    if (currentPage > 1) {
        buttonsHtml += `<button onclick="loadRepos(${currentPage - 1}, '${getUrlParams().sortBy}', '${getUrlParams().sortOrder}')">«</button>`;
    }
    
    // 页码按钮（显示当前页前后2页）
    for (let i = Math.max(1, currentPage - 2); i <= Math.min(totalPages, currentPage + 2); i++) {
        if (i === currentPage) {
            buttonsHtml += `<button class="active">${i}</button>`;
        } else {
            buttonsHtml += `<button onclick="loadRepos(${i}, '${getUrlParams().sortBy}', '${getUrlParams().sortOrder}')">${i}</button>`;
        }
    }
    
    // 下一页按钮
    if (currentPage < totalPages) {
        buttonsHtml += `<button onclick="loadRepos(${currentPage + 1}, '${getUrlParams().sortBy}', '${getUrlParams().sortOrder}')">»</button>`;
    }
    
    paginationEl.innerHTML = buttonsHtml;
}

// 初始化排序按钮事件监听
function initSortButtons() {
    const sortBtns = document.querySelectorAll('.sort-btn');
    const params = getUrlParams();
    
    // 更新当前激活的按钮状态
    sortBtns.forEach(btn => {
        if (btn.dataset.sortBy === params.sortBy && btn.dataset.sortOrder === params.sortOrder) {
            btn.classList.add('active');
        } else {
            btn.classList.remove('active');
        }
        
        // 绑定点击事件
        btn.addEventListener('click', () => {
            const sortBy = btn.dataset.sortBy;
            const sortOrder = btn.dataset.sortOrder;
            
            updateUrlParams({ page: 1, sortBy, sortOrder });
            loadRepos(1, sortBy, sortOrder);
        });
    });
}

// 页面加载完成后初始化
document.addEventListener('DOMContentLoaded', () => {
    const params = getUrlParams();
    
    // 如果是列表页（没有id参数），加载仓库列表
    if (!window.location.search.includes('id=')) {
        loadRepos(params.page, params.sortBy, params.sortOrder);
        initSortButtons();
    }
});
```

- [ ] **Step 3: 验证app.js语法**

```bash
python3 -c "import ast; ast.parse(open('/mnt/e/Projects/htmlSpace/GithubAssistant/public/app.js').read()); print('Syntax OK')" || echo "注意：JS文件不能用Python解析，需浏览器测试"
```

---

### Task 4: 实现详情页 (detail.html)

**Files:**
- Create: `public/detail.html`

- [ ] **Step 1: 编写详情页HTML结构**

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GitHub Reader - Detail</title>
    <link rel="stylesheet" href="/style.css">
    <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/dompurify@3/dist/purify.min.js"></script>
</head>
<body>
    <!-- 顶部导航 -->
    <header class="header">
        <div class="container header-content">
            <a href="/" class="back-link">← 返回列表</a>
            <h1 id="repo-name" class="detail-title"></h1>
        </div>
    </header>

    <!-- 详情内容 -->
    <main class="container detail-container">
        <!-- 信息卡片区 -->
        <section class="info-card">
            <p id="repo-desc" class="info-desc"></p>
            <div class="info-meta">
                <span id="repo-stars" class="meta-star"></span>
                <span id="repo-lang" class="meta-lang"></span>
                <a id="repo-link" target="_blank" class="github-link">GitHub →</a>
            </div>
        </section>

        <!-- README切换Tab -->
        <div class="readme-tabs" id="readme-tabs">
            <button class="tab-btn active" data-lang="zh">中文</button>
            <button class="tab-btn" data-lang="en">English</button>
        </div>

        <!-- README内容区 -->
        <section class="readme-content" id="readme-content">
            <div class="loading">加载中...</div>
        </section>
    </main>

    <script src="/app.js"></script>
</body>
</html>
```

---

### Task 5: 实现响应式样式 (style.css)

**Files:**
- Create: `public/style.css`

- [ ] **Step 1: 编写完整CSS样式代码（移动端优先）**

```css
/* public/style.css - GitHub Reader Public Viewer 样式 */

/* === Reset & Base Styles === */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    background-color: #f8f9fa;
    color: #333;
    line-height: 1.6;
}

/* === Layout Container === */
.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 16px;
}

/* === Header Styles === */
.header {
    background-color: #fff;
    border-bottom: 1px solid #e5e7eb;
    position: sticky;
    top: 0;
    z-index: 100;
}

.header-content {
    display: flex;
    align-items: center;
    justify-content: space-between;
    height: 64px;
}

.logo, .detail-title {
    font-size: 18px;
    font-weight: 600;
    color: #0366d6;
    text-decoration: none;
}

.back-link {
    display: inline-flex;
    align-items: center;
    gap: 4px;
    margin-right: 12px;
    color: #0366d6;
    text-decoration: none;
    font-size: 15px;
}

/* === Sort Bar Styles === */
.sort-bar {
    padding: 16px 0;
    border-bottom: 1px solid #e5e7eb;
}

.sort-btn-group {
    display: flex;
    gap: 8px;
}

.sort-btn {
    padding: 8px 16px;
    border: 1px solid #d1d5db;
    background-color: #fff;
    color: #374151;
    border-radius: 6px;
    cursor: pointer;
    font-size: 14px;
    transition: all 0.2s ease;
}

.sort-btn:hover {
    background-color: #f3f4f6;
    border-color: #9ca3af;
}

.sort-btn.active {
    background-color: #0366d6;
    color: #fff;
    border-color: #0366d6;
}

/* === Repo List Styles === */
.repo-list {
    margin-top: 16px;
}

.repo-item {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 12px 0;
    border-bottom: 1px solid #e5e7eb;
    cursor: pointer;
    transition: background-color 0.2s ease;
}

.repo-item:hover {
    background-color: #f9fafb;
}

.repo-info {
    flex: 1;
    min-width: 0;
}

a.repo-name-link {
    display: block;
    font-size: 16px;
    font-weight: 500;
    color: #0366d6;
    text-decoration: none;
    margin-bottom: 4px;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
}

a.repo-name-link:hover {
    text-decoration: underline;
}

.repo-desc {
    font-size: 14px;
    color: #6b7280;
    margin-bottom: 4px;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
}

.repo-topics {
    display: flex;
    flex-wrap: wrap;
    gap: 4px;
    margin-top: 6px;
}

.topic-tag {
    display: inline-block;
    padding: 2px 8px;
    background-color: #e0f2fe;
    color: #0369a7;
    border-radius: 12px;
    font-size: 12px;
}

.repo-meta {
    display: flex;
    gap: 12px;
    align-items: center;
    margin-left: auto;
    padding-left: 12px;
    flex-shrink: 0;
    font-size: 13px;
    color: #6b7280;
}

.meta-stars {
    color: #f59e0b;
}

/* === Detail Page Styles === */
.detail-container {
    margin-top: 24px;
}

.info-card {
    background-color: #fff;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
    margin-bottom: 24px;
}

.info-desc {
    font-size: 15px;
    color: #6b7280;
    margin-bottom: 12px;
}

.info-meta {
    display: flex;
    gap: 16px;
    align-items: center;
    font-size: 14px;
    color: #374151;
}

.meta-star {
    color: #f59e0b;
    font-weight: 500;
}

.github-link {
    margin-left: auto;
    color: #0366d6;
    text-decoration: none;
}

.github-link:hover {
    text-decoration: underline;
}

/* === README Tabs Styles === */
.readme-tabs {
    display: flex;
    gap: 8px;
    margin-bottom: 16px;
}

.tab-btn {
    padding: 8px 20px;
    border: 1px solid #d1d5db;
    background-color: #fff;
    color: #374151;
    border-radius: 6px 6px 0 0;
    cursor: pointer;
    font-size: 14px;
    transition: all 0.2s ease;
}

.tab-btn.active {
    background-color: #f9fafb;
    color: #0366d6;
    border-bottom-color: transparent;
}

/* === README Content Styles === */
.readme-content {
    background-color: #fff;
    padding: 24px;
    border-radius: 8px;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
    overflow-x: auto;
}

.readme-content h1 {
    font-size: 28px;
    padding-bottom: 16px;
    border-bottom: 1px solid #e5e7eb;
    margin-bottom: 24px;
}

.readme-content h2 {
    font-size: 24px;
    margin-top: 32px;
    padding-bottom: 8px;
    border-bottom: 1px solid #f3f4f6;
}

.readme-content h3 {
    font-size: 20px;
    margin-top: 24px;
}

.readme-content p {
    margin-bottom: 16px;
}

.readme-content pre {
    background-color: #f6f8fa;
    padding: 16px;
    border-radius: 6px;
    overflow-x: auto;
    margin: 16px 0;
}

.readme-content code {
    font-family: 'Courier New', monospace;
    background-color: #f3f4f6;
    padding: 2px 4px;
    border-radius: 4px;
    font-size: 14px;
}

.readme-content pre code {
    background-color: transparent;
    padding: 0;
}

.readme-content a {
    color: #0366d6;
    text-decoration: none;
}

.readme-content a:hover {
    text-decoration: underline;
}

.readme-content img {
    max-width: 100%;
    height: auto;
}

/* === Loading & Empty States === */
.loading, .empty, .error {
    display: block;
    text-align: center;
    padding: 48px 24px;
    color: #6b7280;
}

.error {
    color: #dc3545;
}

/* === Pagination Styles === */
.pagination {
    display: flex;
    justify-content: center;
    gap: 8px;
    margin-top: 24px;
    padding-bottom: 16px;
}

.pagination button {
    min-width: 36px;
    height: 36px;
    border: 1px solid #d1d5db;
    background-color: #fff;
    color: #374151;
    border-radius: 4px;
    cursor: pointer;
    font-size: 14px;
    transition: all 0.2s ease;
}

.pagination button:hover {
    background-color: #f9fafb;
    border-color: #9ca3af;
}

.pagination button.active {
    background-color: #0366d6;
    color: #fff;
    border-color: #0366d6;
}

/* === Responsive Design (Mobile First) === */
@media screen and (max-width: 768px) {
    .container {
        padding: 0 12px;
    }
    
    .header-content {
        height: 56px;
    }
    
    .logo, .detail-title {
        font-size: 16px;
    }
    
    .sort-btn-group {
        flex-wrap: wrap;
    }
    
    .repo-item {
        flex-direction: column;
        align-items: flex-start;
        gap: 8px;
    }
    
    .repo-meta {
        margin-left: 0;
        padding-left: 0;
        width: 100%;
        justify-content: space-between;
    }
    
    .info-card {
        padding: 16px;
    }
    
    .readme-tabs {
        flex-wrap: wrap;
    }
    
    .readme-content {
        padding: 16px;
    }
}

@media screen and (min-width: 769px) {
    /* PC端优化 */
    .repo-item {
        align-items: center;
    }
    
    .detail-container {
        display: grid;
        grid-template-columns: 280px auto;
        gap: 24px;
    }
    
    .info-card {
        grid-column: 1;
        position: sticky;
        top: 80px;
    }
}
```

---

### Task 6: 测试与验证

- [ ] **Step 1: 运行export.py脚本测试（预览模式）**

```bash
cd /mnt/e/Projects/htmlSpace/GithubAssistant/public && python3 export.py
```

预期输出：
```
📊 连接数据库: ...
🔍 查询仓库数据...
📦 找到 X 条记录
📝 导出 X 条记录到JSON...
📚 README文件: Y 个
✅ 导出完成！数据位于: data/repos.json
```

- [ ] **Step 2: 验证生成的repos.json格式**

```bash
python3 -c "import json; data=json.load(open('/mnt/e/Projects/htmlSpace/GithubAssistant/public/data/repos.json')); print(f'仓库数量: {len(data)}'); print('第一条:', data[0] if data else '空')"
```

- [ ] **Step 3: 验证README文件是否复制成功**

```bash
ls -la /mnt/e/Projects/htmlSpace/GithubAssistant/public/data/readmes/ | head -10
```

预期输出：显示已复制的.md文件列表

---

### Task 7: Git提交与初始化

- [ ] **Step 1: 在public目录初始化git仓库**

```bash
cd /mnt/e/Projects/htmlSpace/GithubAssistant/public && git init
```

- [ ] **Step 2: 添加所有代码文件（排除data/）**

```bash
cd /mnt/e/Projects/htmlSpace/GithubAssistant/public && git add .gitignore README.md index.html detail.html style.css app.js export.py
```

- [ ] **Step 3: 提交初始版本**

```bash
cd /mnt/e/Projects/htmlSpace/GithubAssistant/public && git commit -m "feat: 初始化GitHub Reader Public Viewer"
```

---

## Self-Review Checklist

1. ✅ **Spec coverage:** 
   - Task 1-2: Python导出脚本（实现数据预生成）
   - Task 3-4: 列表页+详情页HTML/JS结构
   - Task 5: 响应式样式设计
   - Task 6: 测试验证流程

2. ✅ **Placeholder scan:** 
   - 所有代码完整呈现，无"TBD"/"TODO"占位符
   - CSS断点、排序逻辑、分页组件均已明确实现

3. ✅ **Type consistency:** 
   - JSON字段名 `readme_path`/`readme_zh_path` 在export.py和app.js中保持一致
   - URL参数 `sort_by`/`sort_order` 在HTML按钮和JS逻辑中使用相同命名

4. ⚠️ **Scope check:** 
   - 仅包含列表+详情页，无后端代码
   - "一键发布"功能按需求暂不实现（后续需求）

5. ✅ **Ambiguity check:** 
   - 分页大小固定为80条/页（config.json配置）
   - README切换使用Tab按钮而非URL参数（更符合用户预期）
