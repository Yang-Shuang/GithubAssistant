# GitHub Reader Public Viewer

纯静态GitHub Pages展示模块，用于公开浏览抓取到的仓库信息。AI 相关的仓库

## 使用方法

1. 本地运行 `python export.py` 导出数据（从SQLite读取）
2. 提交并推送到GitHub Pages仓库

## 功能特性

- **列表页**：支持三种排序方式（最新抓取/最早抓取/最多星标）
- **详情页**：中英文README切换，Markdown渲染
- **响应式设计**：适配移动端和PC端双栏布局
- **纯静态**：无后端依赖，GitHub Pages原生支持

## 技术栈

- HTML5 + CSS3 (响应式)
- Vanilla JavaScript (ES6+)
- Markdown渲染 (marked.js + DOMPurify CDN)
