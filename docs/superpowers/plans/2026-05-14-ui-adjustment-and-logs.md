# UI 调整与日志显示 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development to implement this plan task-by-task.

**Goal:** 调整导航栏文字、重新排列翻译按钮位置、添加 README 批量翻译功能、在管理页面添加实时日志显示。

**Architecture:** 纯前端 UI 调整 + 后端新增一个轻量级日志 API 端点。不涉及数据库变更，不修改现有翻译逻辑。

**Tech Stack:** Python Flask + 原生 HTML/CSS/JS

---

## 文件变更概览

| 文件 | 变更类型 | 说明 |
|------|---------|------|
| `web/index.html` | 修改 | 导航栏"搜索管理"→"管理"，移除翻译按钮区域 |
| `web/search.html` | 修改 | 导航栏"搜索管理"→"管理"，添加翻译按钮组 + 日志区域 |
| `web/app.js` | 修改 | 按钮事件绑定、README 翻译逻辑、日志轮询逻辑 |
| `server.py` | 修改 | 新增 `GET /api/logs` 端点 |

---

### Task 1: 导航栏文字修改

**Files:**
- Modify: `web/index.html:15`
- Modify: `web/search.html:13`

- [ ] **Step 1: 修改 index.html 导航文字**

将第 15 行改为：
```html
<a href="/search.html">管理</a>
```

- [ ] **Step 2: 修改 search.html 导航文字**

将第 13 行改为：
```html
<a href="/search.html">管理</a>
```

- [ ] **Step 3: 验证**

在浏览器中打开首页和管理页面，确认导航栏显示"收件箱"和"管理"。

---

### Task 2: 首页移除翻译按钮区域

**Files:**
- Modify: `web/index.html:28-32`

- [ ] **Step 1: 移除 translate-section**

删除 `web/index.html` 中第 28-32 行：
```html
<div class="translate-section" id="translate-section">
    <button class="filter-btn" id="translate-desc-btn">翻译全部</button>
    <button class="filter-btn" id="stop-translate-btn" style="display: none; background: #dc3545; color: #fff; border-color: #dc3545;">停止</button>
    <span id="desc-translate-progress" style="margin-left: 8px; font-size: 13px; color: #666;"></span>
</div>
```

- [ ] **Step 2: 清理 app.js 中相关逻辑**

删除 `web/app.js` 中第 72-77 行（显示翻译按钮的逻辑）：
```javascript
// 显示翻译按钮（如果有未翻译的描述）
const hasPending = data.repos.some(r => r.description && !r.description_zh);
const translateSection = document.getElementById('translate-section');
if (translateSection) {
    translateSection.style.display = hasPending ? 'flex' : 'none';
}
```

- [ ] **Step 3: 验证**

首页不再显示翻译按钮区域。

---

### Task 3: 管理页面添加翻译按钮组

**Files:**
- Modify: `web/search.html:39-41`

- [ ] **Step 1: 在搜索.html 中添加翻译按钮组**

在"手动抓取"部分（第 39-41 行）之后、`</div>` 之前，添加以下内容：

```html
<hr style="margin: 24px 0;">

<h2>翻译管理</h2>
<div style="margin: 16px 0; display: flex; gap: 8px; align-items: center;">
    <button class="fetch-btn" id="translate-desc-btn" onclick="startTranslateDescriptions()">翻译描述</button>
    <button class="fetch-btn" id="stop-translate-desc-btn" style="display: none; background: #dc3545;" onclick="stopTranslateDescriptions()">停止</button>
    <span id="desc-translate-progress" style="margin-left: 8px; font-size: 13px; color: #666;"></span>
    
    <span style="margin: 0 16px;">|</span>
    
    <button class="fetch-btn" id="translate-readme-btn" onclick="startTranslateReadmes()">翻译README</button>
    <button class="fetch-btn" id="stop-translate-readme-btn" style="display: none; background: #dc3545;" onclick="stopTranslateReadmes()">停止</button>
    <span id="readme-translate-progress" style="margin-left: 8px; font-size: 13px; color: #666;"></span>
</div>
```

- [ ] **Step 2: 添加日志区域**

在翻译按钮组之后、`</div>`（第 43 行）之前，添加：

```html
<hr style="margin: 24px 0;">

<h2 id="log-title">日志</h2>
<div id="log-container" style="background: #1e1e1e; color: #dcdcdc; padding: 12px; border-radius: 6px; font-family: 'Courier New', monospace; font-size: 13px; height: 300px; overflow-y: auto; display: none;">
    <div id="log-content"></div>
</div>
```

- [ ] **Step 3: 验证**

管理页面显示：关键词管理 → 数据统计 → 手动抓取 → 翻译管理（两个按钮组）→ 日志区域。

---

### Task 4: 后端新增日志 API 端点

**Files:**
- Modify: `server.py`

- [ ] **Step 1: 在 server.py 中导入日志路径工具**

在文件顶部（第 5-6 行附近）添加：
```python
import re
```

- [ ] **Step 2: 添加日志 API 端点**

在 `@app.route('/api/description/translate/stop', ...)` 之后（第 219 行之后），添加：

```python
@app.route('/api/logs', methods=['GET'])
def api_logs():
    log_type = request.args.get('type', 'fetch')
    lines = int(request.args.get('lines', 50))
    
    if log_type == 'translate':
        log_file = os.path.join(get_data_dir(), 'translator.log')
    else:
        log_file = os.path.join(get_data_dir(), 'server.log')
    
    try:
        with open(log_file, 'r', encoding='utf-8') as f:
            all_lines = f.readlines()
        tail = all_lines[-lines:] if len(all_lines) > lines else all_lines
        # 去除换行符，转义 HTML 特殊字符
        formatted = ''.join(line.rstrip('\n') for line in tail)
        formatted = formatted.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        return jsonify({'logs': formatted})
    except FileNotFoundError:
        return jsonify({'logs': '日志文件不存在'})
    except Exception as e:
        return jsonify({'logs': f'读取失败: {e}'})
```

- [ ] **Step 3: 验证**

```bash
curl http://localhost:5000/api/logs?type=fetch&lines=5
curl http://localhost:5000/api/logs?type=translate&lines=5
```

---

### Task 5: 前端实现翻译 README 逻辑

**Files:**
- Modify: `web/app.js`

- [ ] **Step 1: 添加 startTranslateReadmes 函数**

在 `startTranslateDescriptions` 函数之前（第 263 行之前），添加：

```javascript
async function startTranslateReadmes() {
    const btn = document.getElementById('translate-readme-btn');
    const stopBtn = document.getElementById('stop-translate-readme-btn');
    const progress = document.getElementById('readme-translate-progress');
    const logContainer = document.getElementById('log-container');
    const logTitle = document.getElementById('log-title');
    
    btn.disabled = true;
    btn.style.display = 'none';
    stopBtn.style.display = 'inline-block';
    progress.textContent = '翻译进行中...';
    logContainer.style.display = 'block';
    logTitle.textContent = '翻译日志';
    
    try {
        await apiPost('/readme/translate');
        pollReadmeTranslateStatus();
    } catch (e) {
        progress.textContent = '操作失败: ' + e.message;
        btn.disabled = false;
        btn.style.display = 'inline-block';
        stopBtn.style.display = 'none';
    }
}
```

- [ ] **Step 2: 添加 pollReadmeTranslateStatus 函数**

在 `startTranslateReadmes` 之后，添加：

```javascript
async function pollReadmeTranslateStatus() {
    const btn = document.getElementById('translate-readme-btn');
    const stopBtn = document.getElementById('stop-translate-readme-btn');
    const progress = document.getElementById('readme-translate-progress');
    const logContent = document.getElementById('log-content');
    const logContainer = document.getElementById('log-container');
    
    try {
        const data = await apiGet('/translate/status');
        
        if (data.running) {
            // 轮询翻译日志
            const logData = await apiGet('/logs?type=translate&lines=50');
            logContent.innerHTML = logData.logs.replace(/\n/g, '<br>');
            logContainer.scrollTop = logContainer.scrollHeight;
            
            setTimeout(() => pollReadmeTranslateStatus(), 2000);
        } else {
            progress.textContent = '翻译完成';
            btn.style.display = 'none';
            stopBtn.style.display = 'none';
            
            // 刷新日志
            const logData = await apiGet('/logs?type=translate&lines=50');
            logContent.innerHTML = logData.logs.replace(/\n/g, '<br>');
            logContainer.scrollTop = logContainer.scrollHeight;
        }
    } catch (e) {
        progress.textContent = '轮询失败: ' + e.message;
        btn.style.display = 'inline-block';
        stopBtn.style.display = 'none';
    }
}
```

- [ ] **Step 3: 添加 stopTranslateReadmes 函数**

在 `pollReadmeTranslateStatus` 之后，添加：

```javascript
async function stopTranslateReadmes() {
    const btn = document.getElementById('translate-readme-btn');
    const stopBtn = document.getElementById('stop-translate-readme-btn');
    const progress = document.getElementById('readme-translate-progress');
    const logContent = document.getElementById('log-content');
    const logContainer = document.getElementById('log-container');
    
    try {
        await apiPost('/translate/stop');
        progress.textContent = '已发送停止信号';
        
        await new Promise(resolve => setTimeout(resolve, 3000));
        
        const logData = await apiGet('/logs?type=translate&lines=50');
        logContent.innerHTML = logData.logs.replace(/\n/g, '<br>');
        logContainer.scrollTop = logContainer.scrollHeight;
        
        btn.style.display = 'inline-block';
        stopBtn.style.display = 'none';
        btn.disabled = false;
    } catch (e) {
        progress.textContent = '停止失败: ' + e.message;
    }
}
```

- [ ] **Step 4: 更新按钮事件绑定**

在文件末尾（第 415 行之后），添加：

```javascript
// README 翻译按钮
document.getElementById('translate-readme-btn').onclick = startTranslateReadmes;
document.getElementById('stop-translate-readme-btn').onclick = stopTranslateReadmes;
```

---

### Task 6: 后端新增 README 批量翻译 API

**Files:**
- Modify: `server.py`

- [ ] **Step 1: 添加 README 翻译 API 端点**

在 `@app.route('/api/description/translate/stop', ...)` 之后，添加：

```python
@app.route('/api/readme/translate', methods=['POST'])
def api_readme_translate():
    global translate_thread
    
    with fetch_lock:
        if translate_thread and translate_thread.is_alive():
            return jsonify({'status': 'busy', 'message': '翻译任务进行中'}), 409
        
        def translate_worker():
            try:
                from translator import run_translate
                run_translate(limit=100)
            except Exception as e:
                logger.error(f'README 翻译线程出错: {e}')
        
        translate_thread = threading.Thread(target=translate_worker, daemon=True)
        translate_thread.start()
    
    return jsonify({'status': 'started'})
```

- [ ] **Step 2: 添加停止 README 翻译 API**

在 README 翻译 API 之后，添加：

```python
@app.route('/api/translate/stop', methods=['POST'])
def api_translate_stop():
    global translate_thread
    with fetch_lock:
        translate_thread = None
    return jsonify({'status': 'stopped'})
```

---

### Task 7: 前端实现描述翻译日志显示

**Files:**
- Modify: `web/app.js`

- [ ] **Step 1: 修改 startTranslateDescriptions 添加日志显示**

将现有的 `startTranslateDescriptions` 函数修改为：

```javascript
async function startTranslateDescriptions() {
    const btn = document.getElementById('translate-desc-btn');
    const stopBtn = document.getElementById('stop-translate-desc-btn');
    const progress = document.getElementById('desc-translate-progress');
    const logContainer = document.getElementById('log-container');
    const logTitle = document.getElementById('log-title');
    
    btn.disabled = true;
    btn.style.display = 'none';
    stopBtn.style.display = 'inline-block';
    progress.textContent = '翻译进行中...';
    logContainer.style.display = 'block';
    logTitle.textContent = '翻译日志';
    
    try {
        await apiPost('/description/translate');
        pollDescriptionTranslateStatus();
    } catch (e) {
        progress.textContent = '操作失败: ' + e.message;
        btn.disabled = false;
        btn.style.display = 'inline-block';
        stopBtn.style.display = 'none';
    }
}
```

- [ ] **Step 2: 修改 pollDescriptionTranslateStatus 添加日志轮询**

将现有的 `pollDescriptionTranslateStatus` 函数修改为：

```javascript
async function pollDescriptionTranslateStatus() {
    const btn = document.getElementById('translate-desc-btn');
    const stopBtn = document.getElementById('stop-translate-desc-btn');
    const progress = document.getElementById('desc-translate-progress');
    const logContent = document.getElementById('log-content');
    const logContainer = document.getElementById('log-container');
    
    try {
        const data = await apiGet('/description/translate/status');
        
        if (data.running) {
            if (data.current_repo) {
                progress.textContent = `翻译中: ${data.done}/${data.total} (${data.current_repo})`;
            } else {
                progress.textContent = `翻译中: ${data.done}/${data.total}`;
            }
            
            // 轮询翻译日志
            const logData = await apiGet('/logs?type=translate&lines=50');
            logContent.innerHTML = logData.logs.replace(/\n/g, '<br>');
            logContainer.scrollTop = logContainer.scrollHeight;
            
            setTimeout(() => pollDescriptionTranslateStatus(), 2000);
        } else {
            progress.textContent = `翻译完成: ${data.done}/${data.total}`;
            btn.style.display = 'none';
            stopBtn.style.display = 'none';
            
            // 刷新日志
            const logData = await apiGet('/logs?type=translate&lines=50');
            logContent.innerHTML = logData.logs.replace(/\n/g, '<br>');
            logContainer.scrollTop = logContainer.scrollHeight;
            
            // 刷新列表
            const filterBtn = document.querySelector('.filter-btn.active');
            const filter = filterBtn ? (filterBtn.id === 'filter-read' ? 'read' : filterBtn.id === 'filter-unread' ? 'unread' : 'all') : 'all';
            loadRepos(filter, 1, 'fetched_at', 'desc');
        }
    } catch (e) {
        progress.textContent = `轮询失败: ${e.message}`;
        btn.style.display = 'inline-block';
        stopBtn.style.display = 'none';
    }
}
```

- [ ] **Step 3: 修改 stopTranslateDescriptions 添加日志刷新**

将现有的 `stopTranslateDescriptions` 函数修改为：

```javascript
async function stopTranslateDescriptions() {
    const btn = document.getElementById('translate-desc-btn');
    const stopBtn = document.getElementById('stop-translate-desc-btn');
    const progress = document.getElementById('desc-translate-progress');
    const logContent = document.getElementById('log-content');
    const logContainer = document.getElementById('log-container');
    
    try {
        await apiPost('/description/translate/stop');
        progress.textContent = '已发送停止信号，等待翻译线程退出...';
        
        await new Promise(resolve => setTimeout(resolve, 3000));
        
        const logData = await apiGet('/logs?type=translate&lines=50');
        logContent.innerHTML = logData.logs.replace(/\n/g, '<br>');
        logContainer.scrollTop = logContainer.scrollHeight;
        
        const filterBtn = document.querySelector('.filter-btn.active');
        const filter = filterBtn ? (filterBtn.id === 'filter-read' ? 'read' : filterBtn.id === 'filter-unread' ? 'unread' : 'all') : 'all';
        loadRepos(filter, 1, 'fetched_at', 'desc');
    } catch (e) {
        progress.textContent = '停止失败: ' + e.message;
    }
}
```

---

### Task 8: 前端实现抓取日志显示

**Files:**
- Modify: `web/app.js`

- [ ] **Step 1: 修改 startFetch 添加日志显示**

将现有的 `startFetch` 函数修改为：

```javascript
async function startFetch() {
    const btn = document.getElementById('fetch-btn');
    const logContainer = document.getElementById('log-container');
    const logTitle = document.getElementById('log-title');
    
    btn.disabled = true;
    btn.textContent = '抓取中...';
    logContainer.style.display = 'block';
    logTitle.textContent = '抓取日志';
    
    await apiPost('/fetch');
    
    pollFetchStatus();
}
```

- [ ] **Step 2: 修改 pollFetchStatus 添加日志轮询**

将现有的 `pollFetchStatus` 函数修改为：

```javascript
async function pollFetchStatus() {
    const statusDiv = document.getElementById('fetch-status');
    const logContent = document.getElementById('log-content');
    const logContainer = document.getElementById('log-container');
    
    if (!statusDiv) return;
    
    try {
        const data = await apiGet('/fetch/status');
        
        statusDiv.innerHTML = `
            <div>抓取状态: ${data.running ? '进行中' : '已完成'}</div>
            <div>总仓库数: ${data.total}</div>
            <div>已翻译: ${data.translated}</div>
            <div>翻译中: ${data.translating}</div>
            <div>待翻译: ${data.pending}</div>
            <div>失败: ${data.failed}</div>
        `;
        
        // 轮询抓取日志
        const logData = await apiGet('/logs?type=fetch&lines=50');
        logContent.innerHTML = logData.logs.replace(/\n/g, '<br>');
        logContainer.scrollTop = logContainer.scrollHeight;
        
        if (data.running) {
            setTimeout(() => pollFetchStatus(), 2000);
        } else {
            document.getElementById('fetch-btn').disabled = false;
            document.getElementById('fetch-btn').textContent = '触发抓取';
            
            // 刷新日志
            const logData = await apiGet('/logs?type=fetch&lines=50');
            logContent.innerHTML = logData.logs.replace(/\n/g, '<br>');
            logContainer.scrollTop = logContainer.scrollHeight;
        }
    } catch (e) {
        document.getElementById('fetch-btn').disabled = false;
        document.getElementById('fetch-btn').textContent = '触发抓取';
    }
}
```

---

### Task 9: 最终验证

- [ ] **Step 1: 启动服务**

```bash
cd /mnt/e/Projects/htmlSpace/GithubAssistant && python server.py
```

- [ ] **Step 2: 验证首页**

打开 `http://localhost:5000/`，确认：
- 导航栏显示"收件箱"和"管理"
- 不再显示翻译按钮区域

- [ ] **Step 3: 验证管理页面 - 抓取**

打开 `http://localhost:5000/search.html`，点击"触发抓取"，确认：
- 抓取进度正常显示
- 下方日志区域显示抓取日志（server.log）

- [ ] **Step 4: 验证管理页面 - 翻译描述**

点击"翻译描述"，确认：
- 进度正常显示
- 日志区域显示翻译日志（translator.log）

- [ ] **Step 5: 验证管理页面 - 翻译README**

点击"翻译README"，确认：
- 进度正常显示
- 日志区域显示翻译日志（translator.log）

- [ ] **Step 6: 验证停止功能**

分别测试描述翻译和 README 翻译的停止按钮。

---

## 自检查

1. **Spec 覆盖：**
   - ✅ 导航栏文字修改 → Task 1
   - ✅ 首页移除翻译按钮 → Task 2
   - ✅ 管理页面添加翻译按钮组 → Task 3
   - ✅ 后端日志 API → Task 4
   - ✅ README 翻译功能 → Task 5, Task 6
   - ✅ 描述翻译日志显示 → Task 7
   - ✅ 抓取日志显示 → Task 8
   - ✅ 完整验证 → Task 9

2. **占位符扫描：** 无 TBD/TODO，所有代码已完整写出。

3. **类型一致性：** API 端点命名规范统一（`/api/logs`, `/api/readme/translate`, `/api/translate/stop`）。

4. **边界情况：**
   - 日志文件不存在 → 返回友好提示
   - 翻译进行中重复点击 → 返回 409
   - 轮询失败 → try-catch 捕获，不阻塞

---

**Plan complete and saved to `docs/superpowers/plans/2026-05-14-ui-adjustment-and-logs.md`. Two execution options:**

**1. Subagent-Driven (recommended)** - I dispatch a fresh subagent per task, review between tasks, fast iteration

**2. Inline Execution** - Execute tasks in this session using executing-plans, batch execution with checkpoints

**Which approach?**
