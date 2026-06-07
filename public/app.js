// public/app.js - GitHub Reader Public Viewer 前端逻辑

const PAGE_SIZE = 80; // 每页显示数量（config.json配置）

// === Global Cache & Filter State ===
let _cachedRepos = [];
let _filteredRepos = [];
let _currentSearchKeyword = '';

function matchesSearch(repo) {
    if (!_currentSearchKeyword.trim()) return true;
    
    const q = _currentSearchKeyword.toLowerCase().trim();
    
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

function applyFilterAndSort() {
    _filteredRepos = _cachedRepos.filter(matchesSearch);
    
    const params = getUrlParams();
    if (params.sortBy === 'stars') {
        _filteredRepos.sort((a, b) => 
            params.sortOrder === 'desc' ? b.stars - a.stars : a.stars - b.stars
        );
    } else if (params.sortBy === 'fetched_at') {
        _filteredRepos.sort((a, b) => 
            params.sortOrder === 'desc' 
                ? new Date(b.fetched_at) - new Date(a.fetched_at) 
                : new Date(a.fetched_at) - new Date(b.fetched_at)
        );
    }
}

function resetSearch() {
    _currentSearchKeyword = '';
    applyFilterAndSort();
}

// URL参数解析工具函数
function getUrlParams() {
    const params = new URLSearchParams(window.location.search);
    return {
        page: parseInt(params.get('page')) || 1,
        sortBy: params.get('sort_by') || 'fetched_at',
        sortOrder: params.get('sort_order') || 'desc'
    };
}

// URL参数更新工具函数（不刷新页面）
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
        // 首次加载：从 JSON 读取数据并缓存
        if (_cachedRepos.length === 0) {
            const response = await fetch('./data/repos.json');
            _cachedRepos = await response.json();
        }
        
        // 应用过滤 + 排序（前端操作，不发请求）
        applyFilterAndSort();
        
        // 分页处理：基于全局连续索引
        const totalPages = Math.ceil(_filteredRepos.length / PAGE_SIZE);
        const startIdx = (page - 1) * PAGE_SIZE;
        const endIdx = Math.min(startIdx + PAGE_SIZE, _filteredRepos.length);
        const pageRepos = _filteredRepos.slice(startIdx, endIdx);
        
        // 渲染列表项
        if (listContainer) {
            listContainer.innerHTML = '';
            
            if (_filteredRepos.length === 0) {
                listContainer.innerHTML = '<div class="empty">暂无数据</div>';
            } else if (pageRepos.length === 0) {
                listContainer.innerHTML = '<div class="empty">该页无数据</div>';
            } else {
                pageRepos.forEach((repo, idx) => {
                    const globalIndex = startIdx + idx + 1;
                    const itemEl = document.createElement('div');
                    itemEl.className = 'repo-item';
                    
                    let topicsHtml = '';
                    if (repo.topics && repo.topics.length > 0) {
                        topicsHtml = `<div class="repo-topics">${repo.topics.map(t => 
                            `<span class="topic-tag">${t}</span>`
                        ).join('')}</div>`;
                    }
                    
                    itemEl.innerHTML = `
                        <div class="repo-info">
                            <span id="badge-name-row" style="display:flex;align-items:center;gap:8px;margin-bottom:4px;">
                                <span class="index-badge">${globalIndex}</span>
                                <a href="detail.html?id=${repo.id}" title="${repo.full_name}">${repo.full_name}</a>
                            </span>
                            <div class="repo-desc">${getCurrentDesc(repo) || '暂无描述'}</div>
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
        
        // 渲染分页组件（传入过滤后的总页数）
        renderPagination(totalPages, page);
        
        // 更新排序按钮状态
        updateSortButtonStates(sortBy, sortOrder);
        
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

// 渲染分页按钮（显示全部页码，支持自动换行）
function renderPagination(totalPages, currentPage) {
    const paginationEl = document.getElementById('pagination');
    
    if (!paginationEl || totalPages <= 1) {
        if (paginationEl) paginationEl.innerHTML = '';
        return;
    }
    
    let buttonsHtml = '';
    const currentSortBy = getUrlParams().sortBy;
    const currentSortOrder = getUrlParams().sortOrder;
    
    for (let i = 1; i <= totalPages; i++) {
        if (i === currentPage) {
            buttonsHtml += `<button class="active">${i}</button>`;
        } else {
            buttonsHtml += `<button onclick="loadRepos(${i}, '${currentSortBy}', '${currentSortOrder}')">${i}</button>`;
        }
    }
    
    paginationEl.innerHTML = buttonsHtml;
}

// 更新排序按钮状态（不重新绑定事件）
function updateSortButtonStates(sortBy, sortOrder) {
    const sortBtns = document.querySelectorAll('.sort-btn');
    
    if (!sortBtns.length) return; // 详情页没有排序按钮
    
    // 先移除所有active类，再给匹配的添加
    let matched = false;
    sortBtns.forEach(btn => {
        const isActive = btn.dataset.sortBy === sortBy && btn.dataset.sortOrder === sortOrder;
        if (isActive) {
            btn.classList.add('active');
            matched = true;
        } else {
            btn.classList.remove('active');
        }
    });
    
    // 如果没有匹配到任何按钮，默认激活第一个（最新抓取）
    if (!matched && sortBtns.length > 0) {
        sortBtns[0].classList.add('active');
    }
}

// 初始化排序按钮事件监听（只调用一次）
let sortButtonsBound = false;

function initSortButtons() {
    if (sortButtonsBound) return; // 已经绑定过，跳过
    
    const sortBtns = document.querySelectorAll('.sort-btn');
    
    if (!sortBtns.length) return; // 详情页没有排序按钮
    
    sortBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const sortBy = btn.dataset.sortBy;
            const sortOrder = btn.dataset.sortOrder;
            
            updateUrlParams({ page: 1, sortBy, sortOrder });
            loadRepos(1, sortBy, sortOrder);
        });
    });
    
    sortButtonsBound = true; // 标记已绑定
}

// === Search Event Binding ===
function initSearch() {
    const searchInput = document.getElementById('search-input');
    const searchBtn = document.getElementById('search-btn');
    
    if (!searchInput || !searchBtn) return;
    
    searchBtn.addEventListener('click', () => {
        _currentSearchKeyword = searchInput.value.trim();
        updateUrlParams({ page: 1 });
        loadRepos(1, getUrlParams().sortBy, getUrlParams().sortOrder);
        
        searchInput.blur();
    });
    
    searchInput.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') {
            searchBtn.click();
        }
    });
}

// === 详情页逻辑 ===

let currentRepo = null;
let currentLang = 'zh'; // 默认中文

function getCurrentDesc(repo) {
    return repo.description_zh || repo.description || '';
}

function updateDetailDesc() {
    const el = document.getElementById('repo-desc');
    if (!el || !currentRepo) return;
    
    el.textContent = currentRepo.description_zh || currentRepo.description || '暂无描述';
}

async function loadDetail(repoId) {
    const response = await fetch('./data/repos.json');
    const repos = await response.json();
    
    currentRepo = repos.find(r => r.id == repoId);
    if (!currentRepo) {
        document.getElementById('repo-name').textContent = '仓库不存在';
        return;
    }
    
    // 更新页面标题和名称
    document.title = `GitHub Reader - ${currentRepo.full_name}`;
    document.getElementById('repo-name').textContent = currentRepo.full_name;
    
    // 更新信息卡片（根据descLang显示）
    updateDetailDesc();
    document.getElementById('repo-stars').textContent = `★ ${formatStars(currentRepo.stars)}`;
    document.getElementById('repo-lang').textContent = currentRepo.language || '-';
    document.getElementById('repo-link').href = currentRepo.html_url || '#';
    
     // 初始化README Tab（根据URL参数或自动选择）
    const urlParams = new URLSearchParams(window.location.search);
    
    // 检查有哪些语言的文件
    const hasZh = !!currentRepo.readme_zh_path;
    const hasEn = !!currentRepo.readme_path;
    
    if (hasZh && hasEn) {
        // 有中英文两种，根据URL参数决定
        currentLang = urlParams.get('lang') === 'en' ? 'en' : 'zh';
    } else if (hasZh) {
        // 只有中文
        currentLang = 'zh';
    } else if (hasEn) {
        // 只有英文
        currentLang = 'en';
    }
    
    updateReadmeTabs();
    loadReadme(currentRepo, currentLang);
}

function updateReadmeTabs() {
    const tabs = document.getElementById('readme-tabs');
    if (!tabs) return;
    
    // 检查是否有中文和英文README
    const hasZh = !!currentRepo.readme_zh_path;
    const hasEn = !!currentRepo.readme_path;
    
    if (hasZh && hasEn) {
        tabs.style.display = 'flex';
        
        // 更新Tab按钮状态
        const btns = tabs.querySelectorAll('.tab-btn');
        btns.forEach(btn => {
            if ((btn.dataset.lang === 'zh' && currentLang === 'zh') ||
                (btn.dataset.lang === 'en' && currentLang === 'en')) {
                btn.classList.add('active');
            } else {
                btn.classList.remove('active');
            }
            
           // 绑定点击事件（去重处理）
            btn.addEventListener('click', () => {
                const lang = btn.dataset.lang;
                
                // 更新URL参数
                const url = new URL(window.location);
                if (lang === 'en') {
                    url.searchParams.set('lang', 'en');
                } else {
                    url.searchParams.delete('lang');
                }
                
                window.history.replaceState(null, '', url.toString());
                currentLang = lang;
                
                // 更新UI状态（先调用这个，再加载内容）
                updateReadmeTabs();
                loadReadme(currentRepo, lang);
            });
        });
           } else if (hasZh || hasEn) {
        // 只有一种语言时，仍然显示对应的Tab按钮（让用户明确知道当前语言）
        tabs.style.display = 'flex';
        const btns = tabs.querySelectorAll('.tab-btn');
        btns.forEach(btn => {
            if ((btn.dataset.lang === 'zh' && hasZh) || (btn.dataset.lang === 'en' && hasEn)) {
                btn.style.display = ''; // 显示对应的Tab
                btn.disabled = true;      // 禁用点击（只有一种语言）
            } else {
                btn.style.display = 'none'; // 隐藏不存在的语言
            }
        });
    }
}

async function loadReadme(repo, lang) {
    const contentEl = document.getElementById('readme-content');
    
    if (!contentEl) return;
    
    let readmePath = null;
    if (lang === 'zh') {
        readmePath = repo.readme_zh_path;
    } else {
        readmePath = repo.readme_path;
    }
    
    if (!readmePath) {
        contentEl.innerHTML = '<div class="empty">暂无 README 文件</div>';
        return;
    }
    
    try {
        contentEl.innerHTML = '<div class="loading">加载中...</div>';
        
        const response = await fetch(`./${readmePath}`);
        if (!response.ok) throw new Error('README not found');
        
        const text = await response.text();
        
        // 使用marked.js渲染Markdown，并用DOMPurify清理XSS
        const rawHtml = marked.parse(text);
        const cleanHtml = DOMPurify.sanitize(rawHtml, {
            ADD_ATTR: ['target'], // 允许target属性（用于链接）
            ADD_TAGS: ['iframe']  // 允许iframe（用于嵌入内容）
        });
        
        contentEl.innerHTML = cleanHtml;
    } catch (error) {
        console.error('加载README失败:', error);
        contentEl.innerHTML = '<div class="error">❌ 加载 README 失败</div>';
    }
}

// === 页面加载完成后初始化 ===
document.addEventListener('DOMContentLoaded', () => {
    const params = getUrlParams();
    
    // 检查是否是详情页（URL包含id参数）
    if (window.location.search.includes('id=')) {
        const urlParams = new URLSearchParams(window.location.search);
        const repoId = urlParams.get('id');
        
        if (repoId) {
            loadDetail(repoId);
        } else {
            document.getElementById('repo-name').textContent = '无效ID';
        }
    } else {
        loadRepos(params.page, params.sortBy, params.sortOrder);
        initSortButtons();
        initSearch();
    }
});

// === 详情页语言切换时同步更新描述 ===
const origLoadReadme = loadReadme;
window.loadReadme = function(repo, lang) {
    if (repo && currentRepo?.id === repo.id) {
        updateDetailDesc();
    }
    return origLoadReadme(repo, lang);
};
