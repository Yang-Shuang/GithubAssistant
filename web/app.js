const API_BASE = '/api';

// === Search Filter Helper ===
function matchesSearch(repo, keyword) {
    if (!keyword.trim()) return true; // 空关键词 → 全部通过
    
    const q = keyword.toLowerCase().trim();
    
    let fields = '';
    fields += repo.full_name || '';
    fields += ' ' + (repo.description || '');
    fields += ' ' + (repo.description_zh || '');
    fields += ' ' + (repo.language || '');
    
    if (Array.isArray(repo.topics)) {
        fields += ' ' + repo.topics.join(' ');
    }
    
    return fields.toLowerCase().includes(q);
}

async function apiGet(path, params = {}) {
    const url = new URL(`${API_BASE}${path}`, window.location.origin);
    Object.keys(params).forEach(key => url.searchParams.append(key, params[key]));
    const res = await fetch(url);
    return res.json();
}

async function apiPost(path, body = {}) {
    const res = await fetch(`${API_BASE}${path}`, {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(body)
    });
    const data = await res.json();
    return {...data, _status: res.status};
}

function showToast(message, type = 'success') {
    const container = document.getElementById('toast-container');
    if (!container) return;
    
    const toast = document.createElement('div');
    toast.className = `toast ${type}`;
    toast.textContent = message;
    container.appendChild(toast);
    
    setTimeout(() => {
        toast.style.animation = 'toast-out 0.3s ease forwards';
        setTimeout(() => toast.remove(), 300);
    }, 2500);
}

function showFetchToast(status) {
    const msgs = {
        started: ['📥 抓取任务已启动', 'success'],
        busy: ['⚠️ 抓取任务已在进行中', 'error'],
        error: ['❌ 抓取启动失败', 'error']
    };
    const [msg, type] = msgs[status] || ['操作完成', 'info'];
    showToast(msg, type);
}

function showTranslateToast(type, status) {
    if (type === 'desc') {
        return {
            started: ['📋 Description翻译已启动', 'success'],
            busy: ['⚠️ Description翻译已在进行中', 'error'],
            error: ['❌ Description翻译启动失败', 'error']
        };
    } else {
        return {
            started: ['📝 README翻译已启动', 'success'],
            busy: ['⚠️ README翻译已在进行中', 'error'],
            error: ['❌ README翻译启动失败', 'error']
        };
    }
}

function showStopToast(type) {
    if (type === 'fetch') return showToast('⏹️ 抓取任务停止信号已发送', 'info');
    if (type === 'desc') return showToast('⏹️ Description翻译停止信号已发送', 'info');
    showToast('⏹️ README翻译停止信号已发送', 'info');
}

// Index page — global state for caching/filtering/pagination
let _cachedRepos = [];       // API 原始数据缓存
let _filteredRepos = [];     // 关键词过滤后数据
let _currentFilter = 'all';
let _currentPage = 1;
let _currentSortBy = 'fetched_at';
let _currentUserKeyword = '';

async function loadRepos(filter = 'all', page = 1, sort_by = 'fetched_at', sort_order = 'desc', searchKeyword = '') {
    const container = document.getElementById('repo-list');
    const unreadCount = document.getElementById('unread-count');
    
    if (unreadCount) {
        const stats = await apiGet('/stats');
        unreadCount.textContent = `未读：${stats.unread}`;
    }
    
    if (!container) return;
    
   // === 如果 filter/sort/searchKeyword 变化或数据未缓存，重新拉取 API 数据 ===
    const needsRefresh = (_cachedRepos.length === 0 || _currentFilter !== filter || _currentSortBy !== sort_by);
    const keywordChanged = _currentUserKeyword !== searchKeyword;
    
    if (needsRefresh || keywordChanged) {
        // 更新缓存状态并重置页码
        _currentFilter = filter;
        
        let data;
        try {
            data = await apiGet('/repos', {filter, page: 1, page_size: 99999, sort_by, sort_order});
        } catch (e) {
            container.innerHTML = '<div class="loading">加载失败</div>';
            return;
        }
        
        _cachedRepos = data.repos || [];
        _currentUserKeyword = searchKeyword;
        
        // === 前端关键词过滤 ===
        _filteredRepos = _cachedRepos.filter(repo => matchesSearch(repo, searchKeyword));
        
        if (!_filteredRepos.length) {
            container.innerHTML = '<div class="loading">暂无匹配结果</div>';
            document.getElementById('pagination').innerHTML = '';
            return;
        }
    } else {
        // filter/sort 未变，直接基于已缓存数据渲染当前页（不重新请求 API）
        _currentPage = page;
    }
    
    const pageSize = 20;
    const totalPages = Math.ceil(_filteredRepos.length / pageSize);
    const offset = (page - 1) * pageSize;
    const pageData = _filteredRepos.slice(offset, offset + pageSize);
    
    if (!_filteredRepos.length) {
        container.innerHTML = '<div class="loading">暂无匹配结果</div>';
        return;
    }
    
    // === 渲染列表（带角标）===
    let globalIndex = 1; // 每页从 1 开始
    
    const html = pageData.map(repo => {
        const indexNum = globalIndex++;
        const topicsHtml = (repo.topics || []).map(t => `<span class="topic-tag">${t}</span>`).join(' ');
        return `
        <div class="repo-item ${repo.is_read ? 'read' : 'unread'}" data-id="${repo.id}">
            <div class="index-badge">${indexNum}</div>
            <div class="repo-info">
                <div class="repo-name">${repo.full_name}</div>
                <div class="repo-desc">${repo.description || '暂无描述'}</div>
                ${topicsHtml ? `<div class="repo-topics">${topicsHtml}</div>` : ''}
                ${repo.description_zh ? `<div class="repo-desc-zh">${repo.description_zh}</div>` : ''}
            </div>
            <div class="repo-meta">
                <span class="repo-stars">★ ${repo.stars}</span>
                <span class="translate-status">
                    ${repo.translate_status === 'done' ? '✅' : '⏳'}
                </span>
                <span>${new Date(repo.fetched_at).toLocaleDateString()}</span>
            </div>
        </div>
    `;
    }).join('');
    
    container.innerHTML = html;
    
    // 添加点击事件打开新窗口
    container.querySelectorAll('.repo-item').forEach(item => {
        item.addEventListener('click', () => {
            const id = item.dataset.id;
            window.open(`/detail.html?id=${id}`, '_blank');
        });
    });
    
    // === 渲染分页控件（基于过滤后总数）===
    const pagination = document.getElementById('pagination');
    if (pagination && totalPages > 1) {
        pagination.innerHTML = '';
        
        function createPageBtn(num, text) {
            const btn = document.createElement('button');
            btn.textContent = text || num;
            btn.className = num === _currentPage ? 'active' : '';
            if (text !== undefined && text !== null) {
                btn.disabled = true;
                btn.style.cursor = 'default';
                btn.style.background = '#f5f5f5';
                btn.style.borderColor = '#e0e0e0';
            } else {
                const savedFilter = _currentFilter;
                const savedSortBy = _currentSortBy;
                const savedKeyword = _currentUserKeyword;
                btn.onclick = () => loadRepos(savedFilter, num, savedSortBy, 'desc', savedKeyword);
            }
            pagination.appendChild(btn);
        }
        
        const maxVisible = 7;
        let pages = [];
        
        if (totalPages <= maxVisible) {
            for (let i = 1; i <= totalPages; i++) pages.push(i);
        } else {
            const half = Math.floor(maxVisible / 2);
            let start = _currentPage - half;
            let end = _currentPage + half;
            
            if (start < 1) {
                start = 1;
                end = Math.min(start + maxVisible - 1, totalPages);
            }
            if (end > totalPages) {
                end = totalPages;
                start = Math.max(end - maxVisible + 1, 1);
            }
            
            if (start > 1) {
                pages.push(1);
                if (start > 2) pages.push('...');
            }
            for (let i = start; i <= end; i++) pages.push(i);
            if (end < totalPages - 1) {
                pages.push('...');
                pages.push(totalPages);
            }
        }
        
        // Add prev button
        const prevBtn = document.createElement('button');
        prevBtn.textContent = '‹';
        prevBtn.className = '';
        prevBtn.disabled = _currentPage === 1;
        if (_currentPage > 1) {
            const savedFilter = _currentFilter;
            const savedSortBy = _currentSortBy;
            const savedKeyword = _currentUserKeyword;
            prevBtn.onclick = () => loadRepos(savedFilter, _currentPage - 1, savedSortBy, 'desc', savedKeyword);
        } else {
            prevBtn.style.opacity = '0.5';
            prevBtn.style.cursor = 'not-allowed';
        }
        pagination.appendChild(prevBtn);
        
        pages.forEach(p => createPageBtn(p));
        
        // Add next button
        const nextBtn = document.createElement('button');
        nextBtn.textContent = '›';
        nextBtn.className = '';
        nextBtn.disabled = _currentPage === totalPages;
        if (_currentPage < totalPages) {
            const savedFilter = _currentFilter;
            const savedSortBy = _currentSortBy;
            const savedKeyword = _currentUserKeyword;
            nextBtn.onclick = () => loadRepos(savedFilter, _currentPage + 1, savedSortBy, 'desc', savedKeyword);
        } else {
            nextBtn.style.opacity = '0.5';
            nextBtn.style.cursor = 'not-allowed';
        }
        pagination.appendChild(nextBtn);
    }
    
    // 更新按钮高亮状态（不携带搜索关键词）
    updateActiveButtons(filter, sort_by, sort_order);
}

function updateActiveButtons(filter, sort_by, sort_order) {
    const filterAll = document.getElementById('filter-all');
    const filterRead = document.getElementById('filter-read');
    const filterUnread = document.getElementById('filter-unread');
    if (filterAll) filterAll.classList.toggle('active', filter === 'all');
    if (filterRead) filterRead.classList.toggle('active', filter === 'read');
    if (filterUnread) filterUnread.classList.toggle('active', filter === 'unread');
    
    const sortTime = document.getElementById('sort-time');
    const sortTimeAsc = document.getElementById('sort-time-asc');
    const sortStars = document.getElementById('sort-stars');
    
    if (sortTime) {
        sortTime.classList.toggle('active', sort_by === 'fetched_at' && sort_order === 'desc');
    }
    if (sortTimeAsc) {
        sortTimeAsc.classList.toggle('active', sort_by === 'fetched_at' && sort_order === 'asc');
    }
    if (sortStars) {
        sortStars.classList.toggle('active', sort_by === 'stars' && sort_order === 'desc');
    }
}

// Detail page
async function loadDetail() {
    const params = new URLSearchParams(window.location.search);
    const id = params.get('id');
    if (!id) return;
    
    const repo = await apiGet(`/repos/${id}`);
    document.getElementById('repo-name').textContent = repo.full_name;
    document.getElementById('repo-desc').textContent = repo.description || '暂无描述';
    const descZh = document.getElementById('repo-desc-zh');
    if (descZh && repo.description_zh) {
        descZh.textContent = repo.description_zh;
        descZh.style.display = 'block';
    }
    document.getElementById('repo-stars').textContent = `★ ${repo.stars}`;
    document.getElementById('repo-lang').textContent = repo.language || '未知';
    document.getElementById('repo-link').href = repo.html_url;
    
    const readmeContent = document.getElementById('readme-content');
    const langSwitch = document.getElementById('lang-switch');
    const translateBtn = document.getElementById('translate-btn');
    const translateStatusText = document.getElementById('translate-status-text');
    const readBtn = document.getElementById('read-btn');
    const readStatusText = document.getElementById('read-status-text');
    const savedLang = localStorage.getItem(`lang_${id}`) || 'en';
    
    if (langSwitch) {
        langSwitch.innerHTML = `
            <button class="lang-btn ${savedLang === 'en' ? 'active' : ''}" onclick="switchLang('en')">English</button>
            <button class="lang-btn ${savedLang === 'zh' ? 'active' : ''}" onclick="switchLang('zh')">中文</button>
        `;
    }
    
    // 翻译按钮状态
    if (translateBtn) {
        if (repo.translate_status === 'done') {
            translateStatusText.textContent = '翻译完成';
            translateBtn.disabled = false;
            translateBtn.textContent = '重新翻译';
        } else {
            translateStatusText.textContent = '';
            translateBtn.disabled = false;
            translateBtn.textContent = '翻译';
        }
    }
    
    // 已读按钮状态
    if (readBtn) {
        if (repo.is_read === 1) {
            readStatusText.textContent = '已读';
            readBtn.textContent = '标记未读';
            readBtn.style.background = '#6c757d';
        } else {
            readStatusText.textContent = '未读';
            readBtn.textContent = '标记已读';
            readBtn.style.background = '#28a745';
        }
    }
    
    if (savedLang === 'zh') {
        loadReadme('zh', id);
    } else {
        loadReadme('en', id);
    }
}

async function loadReadme(lang, id) {
    const readmeContent = document.getElementById('readme-content');
    try {
        const suffix = lang === 'zh' ? '_zh' : '';
        const res = await fetch(`/api/repos/${id}/readme${suffix}`);
        if (!res.ok) throw new Error('Not found');
        const text = await res.text();
        readmeContent.innerHTML = DOMPurify.sanitize(marked.parse(text));
    } catch (e) {
        readmeContent.innerHTML = '<div class="loading">加载失败</div>';
    }
}

function switchLang(lang) {
    const params = new URLSearchParams(window.location.search);
    const id = params.get('id');
    if (!id) return;
    
    localStorage.setItem(`lang_${id}`, lang);
    location.reload();
}

async function startTranslate() {
    const params = new URLSearchParams(window.location.search);
    const id = params.get('id');
    if (!id) return;
    
    const btn = document.getElementById('translate-btn');
    const statusText = document.getElementById('translate-status-text');
    btn.disabled = true;
    btn.textContent = '翻译中...';
    statusText.textContent = '正在请求翻译...';
    
    await apiPost(`/repos/${id}/translate`);
    
    pollTranslateStatus(id);
}

async function pollTranslateStatus(id) {
    const btn = document.getElementById('translate-btn');
    const statusText = document.getElementById('translate-status-text');
    
    const data = await apiGet('/translate/status');
    
    if (data.running) {
        statusText.textContent = '翻译进行中，请稍候...';
        setTimeout(() => pollTranslateStatus(id), 2000);
    } else {
        statusText.textContent = '翻译完成';
        btn.disabled = false;
        btn.textContent = '重新翻译';
        
        const savedLang = localStorage.getItem(`lang_${id}`) || 'en';
        if (savedLang === 'zh') {
            location.reload();
        }
    }
}

  async function toggleReadStatus() {
    const params = new URLSearchParams(window.location.search);
    const id = params.get('id');
    if (!id) return;
    
    const btn = document.getElementById('read-btn');
    const statusText = document.getElementById('read-status-text');
    const currentText = btn.textContent;
    
    try {
        if (currentText === '标记已读') {
            await apiPost(`/repos/${id}/unread`);
            statusText.textContent = '已标记为未读';
            btn.textContent = '标记未读';
            btn.style.background = '#6c757d';
        } else {
            await apiPost(`/repos/${id}/read`);
            statusText.textContent = '已标记为已读';
            btn.textContent = '标记已读';
            btn.style.background = '#28a745';
        }
        
        const unreadCount = document.getElementById('unread-count');
        if (unreadCount) {
            const stats = await apiGet('/stats');
            unreadCount.textContent = `未读：${stats.unread}`;
        }
    } catch (e) {
        statusText.textContent = '操作失败';
    }
}

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

async function pollReadmeTranslateStatus() {
    const btn = document.getElementById('translate-readme-btn');
    const stopBtn = document.getElementById('stop-translate-readme-btn');
    const progress = document.getElementById('readme-translate-progress');
    const logContent = document.getElementById('log-content');
    const logContainer = document.getElementById('log-container');
    
    try {
        const data = await apiGet('/translate/status');
        
        if (data.running) {
            const logData = await apiGet('/logs?type=translate&lines=50');
            logContent.innerHTML = logData.logs.replace(/\n/g, '<br>');
            logContainer.scrollTop = logContainer.scrollHeight;
            
            setTimeout(() => pollReadmeTranslateStatus(), 2000);
        } else {
            progress.textContent = '翻译完成';
            btn.style.display = 'none';
            stopBtn.style.display = 'none';
            
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
            
            const logData = await apiGet('/logs?type=translate&lines=50');
            logContent.innerHTML = logData.logs.replace(/\n/g, '<br>');
            logContainer.scrollTop = logContainer.scrollHeight;
            
            setTimeout(() => pollDescriptionTranslateStatus(), 2000);
        } else {
            progress.textContent = `翻译完成: ${data.done}/${data.total}`;
            btn.style.display = 'none';
            stopBtn.style.display = 'none';
            
            const logData = await apiGet('/logs?type=translate&lines=50');
            logContent.innerHTML = logData.logs.replace(/\n/g, '<br>');
            logContainer.scrollTop = logContainer.scrollHeight;
            
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

// === Search Page Logic ===

async function loadSearchStats() {
    const stats = await apiGet('/stats/detailed');
    
    document.getElementById('stat-total').textContent = stats.total.toLocaleString();
    document.getElementById('stat-read').textContent = stats.read_count.toLocaleString();
    document.getElementById('stat-unread').textContent = stats.unread.toLocaleString();
    document.getElementById('stat-max-stars').textContent = (stats.max_stars || 0).toLocaleString();
    
    // README翻译完成
    document.getElementById('stat-readme-translated').textContent = stats.translated_readme?.toLocaleString() || '0';
    // README待翻译
    const readmePendingEl = document.getElementById('stat-readme-pending');
    if (readmePendingEl) {
        readmePendingEl.textContent = stats.pending_readme?.toLocaleString() || '0';
    }
    // Description翻译完成
    const descTransEl = document.getElementById('stat-desc-translated');
    if (descTransEl) {
        descTransEl.textContent = stats.desc_translated?.toLocaleString() || '0';
    }
    // Description待翻译
    const descPendingEl = document.getElementById('stat-pending-desc');
    if (descPendingEl) {
        descPendingEl.textContent = stats.pending_desc?.toLocaleString() || '0';
    }
}

async function loadTopics() {
    const data = await apiGet('/topics');
    const container = document.getElementById('topics-cloud');
    
    if (!container || !data.topics.length) {
        if (container) container.innerHTML = '<p style="color:#666;">暂无标签</p>';
        return;
    }
    
    // 根据容器宽度动态决定显示多少个tags（目标约10行）
    const maxTagsPerRow = Math.max(4, Math.floor(container.clientWidth / 80));
    const targetLines = 10;
    const totalToShow = maxTagsPerRow * targetLines;
    
    // topics按count降序排列，根据频率设置大小和透明度
    const allCounts = data.topics.map(t => t.count);
    const maxCount = Math.max(...allCounts);
    const minCount = Math.min(...allCounts);
    const countRange = maxCount - minCount || 1;
    
    container.innerHTML = data.topics.slice(0, totalToShow).map(topic => {
        let fontSize = '13px';
        let fontWeight = '';
        let opacity = 0.7;
        
        // 根据频率百分比设置样式
        const pct = (topic.count - minCount) / countRange;
        if (pct > 0.95) {
            fontSize = '16px';
            fontWeight = 'bold';
            opacity = 1;
        } else if (pct > 0.8) {
            fontSize = '15px';
            fontWeight = '600';
            opacity = 0.9;
        } else if (pct > 0.5) {
            fontSize = '14px';
            fontWeight = '';
            opacity = 0.8;
        } else if (pct < 0.2) {
            fontSize = '12px';
            fontWeight = '';
            opacity = 0.5;
        }
        
        return `<span class="topic-tag" style="font-size:${fontSize}; font-weight:${fontWeight}; opacity:${opacity}">${topic.name}</span>`;
    }).join('');
    
    // 如果topics数量不足以填满10行，动态调整CSS使容器高度自适应
    if (data.topics.length > totalToShow) {
        container.style.maxHeight = 'none';
    } else {
        const rowsNeeded = Math.ceil(data.topics.length / maxTagsPerRow);
        // 让标签云自然展开，不设最大高度限制
        container.style.overflow = 'visible';
    }
}

async function loadDbSchema() {
    const data = await apiGet('/db/schema');
    const tbody = document.getElementById('schema-tbody');
    
    if (!tbody) return;
    
    tbody.innerHTML = data.columns.map(col => `
        <tr>
            <td><code>${col.name}</code></td>
            <td><span class="type">${col.type} ${col.primary_key ? '(PK)' : ''}${col.not_null ? ' NOT NULL' : ''}</span></td>
            <td>${col.description || '-'}</td>
        </tr>
    `).join('');
}

// === Task Status Polling Helpers ===

async function checkFetchStatus() {
    try {
        const data = await apiGet('/fetch/status');
        return data.running;
    } catch (e) {
        console.error('Check fetch status failed:', e);
        return false;
    }
}

async function checkReadmeTranslateStatus() {
    try {
        const data = await apiGet('/translate/status');
        return data.running;
    } catch (e) {
        console.error('Check readme translate status failed:', e);
        return false;
    }
}

async function checkDescTranslateStatus() {
    try {
        const data = await apiGet('/description/translate/status');
        return data.running;
    } catch (e) {
        console.error('Check desc translate status failed:', e);
        return false;
    }
}

// Fetch control - 始终可点击，智能判断状态
async function startFetch() {
    const btn = document.getElementById('fetch-start-btn');
    
    // 检查是否已经在运行中
    const isRunning = await checkFetchStatus();
    if (isRunning) {
        console.log('抓取任务已在进行中，跳过');
        showToast('⚠️ 抓取任务已在进行中', 'error');
        return;
    }
    
    try {
        await apiPost('/fetch');
        showToast('📥 抓取任务已启动', 'success');
        
        // 轮询任务状态并更新按钮文字
        pollTaskUntilDone(
            checkFetchStatus,
            () => '📥 开始抓取',
            (btn) => btn.textContent = '⏳ 抓取中...'
        );
    } catch (e) {
        console.error('Start fetch failed:', e);
        showToast('❌ 抓取启动失败', 'error');
    }
}

async function stopFetch() {
    const btn = document.getElementById('fetch-start-btn');
    
    // 检查是否没有在运行，如果是则跳过
    const isRunning = await checkFetchStatus();
    if (!isRunning) {
        console.log('抓取任务未在运行中，跳过停止操作');
        return;
    }
    
    try {
        showToast('⏹️ 抓取任务已发送停止信号', 'info');
        await apiPost('/fetch/stop');
        
        // 等待几秒让服务完全停止后再刷新统计
        setTimeout(() => loadSearchStats(), 3000);
    } catch (e) {
        console.error('Stop fetch failed:', e);
    }
}

// README translation control - 始终可点击，智能判断状态
async function startTranslateReadmes() {
    const btn = document.getElementById('readme-translate-start-btn');
    
    // 检查是否已经在运行中
    const isRunning = await checkReadmeTranslateStatus();
    if (isRunning) {
        console.log('README翻译任务已在进行中，跳过');
        showToast('⚠️ README翻译任务已在进行中', 'error');
        return;
    }
    
    try {
        const res = await apiPost('/readme/translate');
        
        if (res._status === 409) {
            showToast('⚠️ README翻译任务已在进行中', 'error');
            btn.disabled = false;
            return;
        }
        
        // 启动成功，显示toast并轮询
        showToast('📝 README翻译已启动', 'success');
        
        // 轮询任务状态并更新按钮文字
        pollTaskUntilDone(
            checkReadmeTranslateStatus,
            () => '📝 翻译 README',
            (btn) => btn.textContent = '⏳ 翻译中...'
        );
    } catch (e) {
        console.error('Start translate failed:', e);
        showToast('❌ README翻译启动失败: ' + e.message, 'error');
    }
}

async function stopTranslateReadmes() {
    const btn = document.getElementById('readme-translate-start-btn');
    
    // 检查是否没有在运行，如果是则跳过
    const isRunning = await checkReadmeTranslateStatus();
    if (!isRunning) {
        console.log('README翻译任务未在运行中，跳过停止操作');
        return;
    }
    
    try {
        showToast('⏹️ README翻译已发送停止信号', 'info');
        await apiPost('/translate/stop');
        
        // 等待几秒让服务完全停止后再刷新统计
        setTimeout(() => loadSearchStats(), 3000);
    } catch (e) {
        console.error('Stop translate failed:', e);
    }
}

// Description translation control - 始终可点击，智能判断状态
async function startTranslateDescriptions() {
    const btn = document.getElementById('desc-translate-start-btn');
    
    // 检查是否已经在运行中
    const isRunning = await checkDescTranslateStatus();
    if (isRunning) {
        console.log('Description翻译任务已在进行中，跳过');
        showToast('⚠️ Description翻译任务已在进行中', 'error');
        return;
    }
    
    try {
        const res = await apiPost('/description/translate');
        
        if (res._status === 409) {
            showToast('⚠️ Description翻译任务已在进行中', 'error');
            btn.disabled = false;
            return;
        }
        
        // 启动成功，显示toast并轮询
        showToast('📋 Description翻译已启动', 'success');
        
        // 轮询任务状态并更新按钮文字
        pollTaskUntilDone(
            checkDescTranslateStatus,
            () => '📋 翻译 Description',
            (btn) => btn.textContent = '⏳ 翻译中...'
        );
    } catch (e) {
        console.error('Start desc translate failed:', e);
        showToast('❌ Description翻译启动失败: ' + e.message, 'error');
    }
}


async function stopTranslateDescriptions() {
    const btn = document.getElementById('desc-translate-start-btn');
    
    // 检查是否没有在运行，如果是则跳过
    const isRunning = await checkDescTranslateStatus();
    if (!isRunning) {
        console.log('Description翻译任务未在运行中，跳过停止操作');
        showToast('⏹️ Description翻译已在非运行状态', 'info');
        return;
    }
    
    try {
        showToast('⏹️ Description翻译已发送停止信号', 'info');
        await apiPost('/description/translate/stop');
        
        // 等待几秒让服务完全停止后再刷新统计
        setTimeout(() => loadSearchStats(), 3000);
    } catch (e) {
        console.error('Stop desc translate failed:', e);
    }
}

// 通用轮询函数：直到任务完成，然后恢复按钮文字并刷新统计
async function pollTaskUntilDone(checkRunning, restoreTextFn, runningTextCb) {
    let btn;
    
    // 找出哪个按钮被点击了（通过调用栈或DOM查找）
    const allStartBtns = [
        document.getElementById('fetch-start-btn'),
        document.getElementById('readme-translate-start-btn'),
        document.getElementById('desc-translate-start-btn')
    ];
    btn = allStartBtns.find(b => b && b.textContent.includes('⏳'));
    
    try {
        while (await checkRunning()) {
            if (btn) runningTextCb(btn);
            await new Promise(resolve => setTimeout(resolve, 2000));
        }
        
        // 任务完成，恢复按钮文字并刷新统计
        if (btn && restoreTextFn) btn.textContent = restoreTextFn();
        loadSearchStats();
    } catch (e) {
        console.error('Poll task status failed:', e);
        if (btn && restoreTextFn) btn.textContent = restoreTextFn();
    }
}


// Init
if (document.getElementById('repo-list')) {
    loadRepos();
    
    // === Search Bar Event Listeners ===
    const searchInput = document.getElementById('search-input');
    const searchBtn = document.getElementById('search-btn');
    
    if (searchBtn && searchInput) {
        const handleSearch = () => {
            const keyword = searchInput.value.trim();
            // 获取当前筛选/排序状态（从 DOM 读取活跃按钮）
            let filter = 'all';
            const activeFilterBtn = document.querySelector('.filter-btn.active');
            if (activeFilterBtn) {
                if (activeFilterBtn.id === 'filter-read') filter = 'read';
                else if (activeFilterBtn.id === 'filter-unread') filter = 'unread';
            }
            
            // 获取当前排序状态
            let sort_by = 'fetched_at', sort_order = 'desc';
            if (document.getElementById('sort-stars').classList.contains('active')) {
                sort_by = 'stars'; sort_order = 'desc';
            } else if (document.getElementById('sort-time-asc').classList.contains('active')) {
                sort_by = 'fetched_at'; sort_order = 'asc';
            }
            
            _currentPage = 1; // 搜索重置页码
            loadRepos(filter, 1, sort_by, sort_order, keyword);
        };
        
        searchBtn.onclick = handleSearch;
        
        searchInput.onkeydown = (e) => {
            if (e.key === 'Enter') handleSearch();
        };
    }
    
    document.getElementById('filter-all').onclick = () => loadRepos('all', 1, 'fetched_at', 'desc');
    document.getElementById('filter-read').onclick = () => loadRepos('read', 1, 'fetched_at', 'desc');
    document.getElementById('filter-unread').onclick = () => loadRepos('unread', 1, 'fetched_at', 'desc');
    
    // Sort buttons — pass current search keyword so it persists across sort changes
    document.getElementById('sort-time').onclick = () => { _currentPage = 1; loadRepos(_currentFilter || 'all', 1, 'fetched_at', 'desc', _currentUserKeyword); };
    document.getElementById('sort-time-asc').onclick = () => { _currentPage = 1; loadRepos(_currentFilter || 'all', 1, 'fetched_at', 'asc', _currentUserKeyword); };
    document.getElementById('sort-stars').onclick = () => { _currentPage = 1; loadRepos(_currentFilter || 'all', 1, 'stars', 'desc', _currentUserKeyword); };
    
    // Description translation buttons (inbox page)
    const descBtn = document.getElementById('translate-desc-btn');
    if (descBtn) {
        descBtn.onclick = startTranslateDescriptions;
    }
    const stopDescBtn = document.getElementById('stop-translate-desc-btn');
    if (stopDescBtn) {
        stopDescBtn.onclick = stopTranslateDescriptions;
    }
    
    // README translation buttons (inbox page)
    const readmeBtn = document.getElementById('translate-readme-btn');
    if (readmeBtn) {
        readmeBtn.onclick = startTranslateReadmes;
    }
    const stopReadmeBtn = document.getElementById('stop-translate-readme-btn');
    if (stopReadmeBtn) {
        stopReadmeBtn.onclick = stopTranslateReadmes;
    }
}

if (document.getElementById('repo-name')) {
    loadDetail();
}

// Search page initialization (replaces keyword-list check)
if (document.querySelector('.search-page')) {
    loadSearchStats();
    loadTopics();
    loadDbSchema();
    
    // Description translation buttons (management page)
    const descBtn = document.getElementById('desc-translate-start-btn');
    if (descBtn) descBtn.onclick = startTranslateDescriptions;
    const stopDescBtn = document.getElementById('desc-translate-stop-btn');
    if (stopDescBtn) stopDescBtn.onclick = stopTranslateDescriptions;
    
    // README translation buttons (management page)
    const readmeBtn = document.getElementById('readme-translate-start-btn');
    if (readmeBtn) readmeBtn.onclick = startTranslateReadmes;
    const stopReadmeBtn = document.getElementById('readme-translate-stop-btn');
    if (stopReadmeBtn) stopReadmeBtn.onclick = stopTranslateReadmes;
}