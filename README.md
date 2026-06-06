# GitHub Reader

通过关键词订阅 GitHub 热门仓库，自动抓取 README 并翻译为中文。

## 安装

```bash
pip install -r requirements.txt
```

## 配置

编辑 `config.json`：
- `github_token`: GitHub Personal Access Token
- `keywords`: 订阅关键词列表
- `llama_cpp.base_url`: llama.cpp server 地址
- `llama_cpp.model`: 使用的模型名称

## 使用

1. 启动 llama.cpp server: `llama.cpp/server -m your_model.gguf -c 4096`
2. 运行抓取: `python fetch.py`
3. 启动 Web 服务: `python server.py`
4. 浏览器访问: `http://localhost:5000`

## Windows 任务计划

创建定时任务每天运行:
```
python fetch.py --fetch-only
python fetch.py --translate-only
```