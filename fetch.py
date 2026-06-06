import requests
import time
import sys
import os
from config import load_config, load_keywords
from utils import setup_logger, format_iso, get_readme_dir, repo_to_filename, log_skip, log_done
from db import init_db, upsert_repo, get_existing_readme_names

logger = setup_logger('fetch')

# === 抓取任务控制 ===
fetch_stop = False
total_repos_fetched = 0


def stop_fetch():
    """设置抓取中断标志"""
    global fetch_stop
    fetch_stop = True


def is_fetch_stopped():
    """检查是否已停止"""
    return bool(fetch_stop)


def search_repos(keyword, top_n=20):
    config = load_config()
    token = config.get('github_token', '')
    headers = {'Authorization': f'token {token}'} if token else {}
    
    url = f'https://api.github.com/search/repositories'
    params = {
        'q': keyword,
        'sort': 'stars',
        'order': 'desc',
        'per_page': top_n
    }
    
    try:
        response = requests.get(url, headers=headers, params=params, timeout=30)
        response.raise_for_status()
        items = response.json().get('items', [])
        
        repos = []
        for item in items:
            repos.append({
                'full_name': item['full_name'],
                'description': item.get('description'),
                'stars': item.get('stargazers_count', 0),
                'language': item.get('language'),
                'topics': item.get('topics', []),
                'html_url': item.get('html_url'),
            })
        
        logger.info(f'关键词 "{keyword}" 搜索到 {len(repos)} 个仓库')
        return repos
    except requests.exceptions.RequestException as e:
        logger.error(f'搜索关键词 "{keyword}" 失败: {e}')
        return []

def fetch_readme(full_name):
    config = load_config()
    token = config.get('github_token', '')
    headers = {'Authorization': f'token {token}'} if token else {}
    
    owner, repo = full_name.split('/')
    
    def try_fetch_ref(branch):
        url = f'https://api.github.com/repos/{owner}/{repo}/readme'
        params = {'ref': branch}
        response = requests.get(url, headers=headers, params=params, timeout=60)
        if response.status_code == 404:
            return None
        response.raise_for_status()
        data = response.json()
        content = data.get('content', '')
        if not content:
            return None
        import base64
        return base64.b64decode(content).decode('utf-8', errors='ignore')

    def fetch_with_retry(url, params=None, timeout=30, max_retries=2):
        for attempt in range(max_retries + 1):
            try:
                resp = requests.get(url, headers=headers, params=params, timeout=timeout)
                return resp
            except Exception as e:
                if attempt < max_retries:
                    logger.debug(f'{full_name} {url.split("api.github.com/repos/", 1)[-1] or "repo"} 请求失败 (第{attempt+1}/{max_retries+1}次): {e}')
                    import time; time.sleep(5)
                else:
                    raise
    
    # 先获取默认分支，再 fallback 到常见分支名
    branch_list = []
    try:
        resp = fetch_with_retry(f'https://api.github.com/repos/{owner}/{repo}', timeout=30, max_retries=2)
        if resp.status_code == 200:
            default_branch = resp.json().get('default_branch')
            if default_branch:
                branch_list.append(default_branch)
    except Exception as e:
        logger.debug(f'获取默认分支失败: {e}')

    fallback_branches = ['main', 'master', 'develop']
    for fb in fallback_branches:
        if fb not in branch_list:
            branch_list.append(fb)
    
    readme_content = None
    for branch in branch_list:
        try:
            readme_content = try_fetch_ref(branch)
            if readme_content:
                break
        except Exception as e:
            logger.warning(f'{full_name} 分支 {branch} README 获取失败: {e}')
    
    if not readme_content:
        logger.warning(f'{full_name} 没有 README')
        return None
    
    readme_dir = get_readme_dir()
    filename = repo_to_filename(full_name)
    filepath = os.path.join(readme_dir, filename)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    logger.info(f'{full_name} README 已保存到 {filepath}')
    return filename

def fetch_repos_with_pagination(query, page_size=80, min_stars_stop=1000):
    """
    使用 OR 拼接的查询参数，分页搜索 GitHub 仓库。
    
    - 按 stars 降序排序
    - 翻页直到：任意仓库 stars < min_stars_stop，或返回结果数 < page_size
    
    Returns: list[dict] 去重后的仓库列表
    """
    config = load_config()
    token = config.get('github_token', '')
    headers = {'Authorization': f'token {token}'} if token else {}
    
    url = 'https://api.github.com/search/repositories'
    seen_repos = set()  # 用于去重（同一仓库可能在不同批次出现）
    all_repos = []
    page = 1
    
    while True:
        params = {
            'q': query,
            'sort': 'stars',
            'order': 'desc',
            'per_page': page_size,
            'page': page
        }
        
        try:
            response = requests.get(url, headers=headers, params=params, timeout=60)
            response.raise_for_status()
            data = response.json()
            items = data.get('items', [])
            
            if not items:
                break
            
            new_repos = []
            for item in items:
                full_name = item['full_name']
                
                # 去重检查
                if full_name in seen_repos:
                    continue
                
                # 停止条件：任意仓库 stars < min_stars_stop
                stars = item.get('stargazers_count', 0)
                if stars and int(stars) < min_stars_stop:
                    return all_repos
                
                seen_repos.add(full_name)
                
                new_repos.append({
                    'full_name': full_name,
                    'description': item.get('description'),
                    'stars': item.get('stargazers_count', 0),
                    'language': item.get('language'),
                    'topics': item.get('topics', []),
                    'html_url': item.get('html_url'),
                })
            
            all_repos.extend(new_repos)
            logger.info(f'分页搜索完成，已获取 {len(all_repos)} 个仓库')
            
            # 停止条件：返回结果少于 page_size（最后一页）
            if len(items) < page_size:
                break
            
            page += 1
            
        except requests.exceptions.RequestException as e:
            logger.error(f'分页搜索失败: {e}')
            return all_repos
    
    return all_repos


def build_keyword_batches(keywords, max_q_length=100):
    """将关键词列表按 max_q_length 分批，每批生成 OR 拼接查询串
    
    GitHub Search API 限制：
    - q 参数最长 256 字符（URL 编码后更短）
    - 最多只能使用 5 个 AND/OR/NOT 操作符（即每个查询最多 6 个关键词）
    
    max_q_length=100 约等于每批 3-6 个关键词，可以确保通过 GitHub API 验证
    """
    batches = []
    
    # Step A: 构建带引号的 parts
    quoted_parts = []
    for kw in keywords:
        if ' ' in kw or '\t' in kw or '\n' in kw or '.' in kw or '-' in kw or '+' in kw or '@' in kw or ':' in kw or '/' in kw:
            quoted_parts.append('"' + kw + '"')
        else:
            quoted_parts.append(kw)
    
    # Step B: 贪心填充每批，直到达到 max_q_length 或超过 6 个关键词
    MAX_KEYWORDS_PER_BATCH = 6
    
    current_batch = []
    current_length = 0
    
    for part, original_kw in zip(quoted_parts, keywords):
        if not current_batch:
            new_length = len(part)
        else:
            new_length = current_length + len(' OR ') + len(part)
        
        # 检查是否达到长度限制或关键词数量上限
        if (new_length <= max_q_length and len(current_batch) < MAX_KEYWORDS_PER_BATCH):
            current_batch.append((part, original_kw))
            current_length = new_length
        else:
            batches.append(current_batch)
            current_batch = [(part, original_kw)]
            current_length = len(part)
    
    if current_batch:
        batches.append(current_batch)
    
    return batches


def run_fetch(keywords=None, top_n=None, interval=None):
    config = load_config()
    
    # 从 keywords.json 读取关键词（替代 config.json）
    kw_keys = load_keywords()
    logger.info(f'从 keywords.json 加载 {len(kw_keys)} 个关键词')
    
    max_q_length = config.get('max_q_length', 100)
    page_size = config.get('page_size', 80)
    min_stars_stop = config.get('min_stars_stop', 1000)
    
    # 分批构建查询串
    batches = build_keyword_batches(kw_keys, max_q_length)
    logger.info(f'关键词分为 {len(batches)} 批')
    
    init_db()
    
    # === 读取增量模式配置 ===
    update_all = config.get('update_all', True)
    
    # Reset counters for new fetch task
    global fetch_stop, total_repos_fetched
    fetch_stop = False
    total_repos_fetched = 0
    
    all_repos = []
    total_batches = len(batches)
    
    # === 去重集合（任务开始时清空）===
    processed_repos: set[str] = set()
    
    for i, batch in enumerate(batches):
        # === 中断检查（每批开始前）===
        if fetch_stop:
            from utils import log_stop
            log_stop(logger, total_repos_fetched, len(all_repos), '抓取')
            return all_repos
        
        # === 增量模式：查询已有 README 的仓库 ===
        if not update_all:
            existing_readme_names = get_existing_readme_names()
            logger.info(f'增量模式：已有 {len(existing_readme_names)} 个仓库有 README')
        
        query_parts = [item[0] for item in batch]
        
        if len(batch) == 1:
            query = batch[0][0]
        else:
            query = ' OR '.join(query_parts)
        
        logger.info(f'开始抓取第 {i+1}/{total_batches} 批，查询串长度={len(query)}')
        
        # 调用带翻页的搜索函数
        repos = fetch_repos_with_pagination(query, page_size=page_size, min_stars_stop=min_stars_stop)
        logger.info(f'第 {i+1} 批抓取完成，共 {len(repos)} 个仓库')
        
        for repo in repos:
            # === 中断检查（每个repo前）===
            if fetch_stop:
                from utils import log_stop
                log_stop(logger, total_repos_fetched, len(all_repos), '抓取')
                return all_repos
            
            full_name = repo['full_name']
            
            # === 去重检查：跳过已处理的仓库 ===
            if full_name in processed_repos:
                log_skip(logger, f'{full_name} (重复)')
                continue
            
            try:
                repo['fetched_at'] = format_iso()
                
                # === 增量模式：跳过已有 README 的仓库 ===
                need_readme_fetch = True
                if not update_all and full_name in existing_readme_names:
                    log_skip(logger, f'{full_name} (增量)')
                    readme_path = None
                    need_readme_fetch = False
                
                if need_readme_fetch:
                    readme_path = fetch_readme(repo['full_name'])
                
                if readme_path:
                    repo['readme_path'] = readme_path
                
                upsert_repo(repo)
                processed_repos.add(full_name)  # === 加入去重集合 ===
                total_repos_fetched += 1
                all_repos.append(repo)
                
                # === 进度日志（每完成一个repo）===
                remaining = max(0, len(all_repos) - total_repos_fetched + (len(repos) - repos.index(repo)))
                estimated_total = total_repos_fetched + remaining
                log_done(logger, total_repos_fetched, remaining, estimated_total, '抓取')
            except Exception as e:
                logger.error(f'处理 {repo["full_name"]} 失败: {e}')
        
        # 批次间间隔（避免 GitHub API 限流）
        if interval and i < len(batches) - 1:
            time.sleep(interval)
    
   # === 任务结束，清空去重集合 ===
    processed_repos.clear()
    
    logger.info(f'全部抓取完成，共 {len(all_repos)} 个仓库')
    return all_repos

if __name__ == '__main__':
    only_fetch = False
    only_translate = False
    
    if '--fetch-only' in sys.argv:
        only_fetch = True
    if '--translate-only' in sys.argv:
        only_translate = True
    
    if only_translate:
        run_translate()
    elif only_fetch:
        run_fetch()
    else:
        run_fetch()
        run_translate()
