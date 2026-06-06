import threading
import time
import os
from flask import Flask, jsonify, request, send_from_directory, abort
from config import get_data_dir, get_readme_dir
from utils import setup_logger, format_iso
from db import (
    init_db, get_repos, get_repo, mark_read, mark_unread,
    update_translate_status, get_all_keywords, get_stats, 
    get_fetch_progress, get_all_topics, get_db_schema
)
from fetch import run_fetch
from translator import run_translate, translate_single_repo, run_translate_descriptions

import threading as _threading

def make_relative_path(abs_path):
    if not abs_path:
        return None
    readme_dir = get_readme_dir()
    if isinstance(abs_path, str) and abs_path.startswith(readme_dir):
        return os.path.relpath(abs_path, readme_dir)
    return os.path.basename(abs_path)

app = Flask(__name__, static_folder='web', static_url_path='')
init_db()  # 应用启动时只执行一次，初始化数据库表结构
logger = setup_logger('server')

fetch_thread = None
translate_thread = None
description_translate_thread = None
fetch_stop_flag = False
translate_stop_flag = False
description_translate_stop_flag = False
fetch_lock = _threading.Lock()



@app.route('/')
def index():
    return send_from_directory('web', 'index.html')

@app.route('/detail.html')
def detail():
    return send_from_directory('web', 'detail.html')

@app.route('/search.html')
def search():
    return send_from_directory('web', 'search.html')

@app.route('/api/repos', methods=['GET'])
def api_repos():
    filter_type = request.args.get('filter', 'all')
    page = int(request.args.get('page', 1))
    page_size = int(request.args.get('page_size', 20))
    sort_by = request.args.get('sort_by', 'fetched_at')
    sort_order = request.args.get('sort_order', 'desc')
    
    repos, total = get_repos(filter_type, page, page_size, sort_by, sort_order)
    for repo in repos:
        repo['readme_path'] = make_relative_path(repo.get('readme_path'))
        repo['readme_zh_path'] = make_relative_path(repo.get('readme_zh_path'))
    return jsonify({'repos': repos, 'total': total, 'page': page, 'page_size': page_size})

@app.route('/api/repos/<int:repo_id>', methods=['GET'])
def api_repo(repo_id):
    repo = get_repo(repo_id)
    if not repo:
        abort(404)
    repo['readme_path'] = make_relative_path(repo.get('readme_path'))
    repo['readme_zh_path'] = make_relative_path(repo.get('readme_zh_path'))
    return jsonify(repo)

@app.route('/api/repos/<int:repo_id>/readme', methods=['GET'])
def api_readme(repo_id):
    repo = get_repo(repo_id)
    if not repo:
        abort(404)
    readme_dir = get_readme_dir()
    from utils import repo_to_filename
    filename = repo_to_filename(repo['full_name'])
    filepath = os.path.join(readme_dir, filename)
    if not os.path.exists(filepath):
        abort(404)
    return send_from_directory(readme_dir, filename)

@app.route('/api/repos/<int:repo_id>/readme_zh', methods=['GET'])
def api_readme_zh(repo_id):
    repo = get_repo(repo_id)
    if not repo:
        abort(404)
    readme_dir = get_readme_dir()
    from utils import repo_to_filename_zh
    filename = repo_to_filename_zh(repo['full_name'])
    filepath = os.path.join(readme_dir, filename)
    if not os.path.exists(filepath):
        abort(404)
    return send_from_directory(readme_dir, filename)

@app.route('/api/repos/<int:repo_id>/read', methods=['POST'])
def api_mark_read(repo_id):
    mark_read(repo_id)
    return jsonify({'status': 'ok'})

@app.route('/api/repos/<int:repo_id>/unread', methods=['POST'])
def api_mark_unread(repo_id):
    mark_unread(repo_id)
    return jsonify({'status': 'ok'})

@app.route('/api/keywords', methods=['GET'])
def api_keywords():
    keywords = get_all_keywords()
    return jsonify({'keywords': keywords})

@app.route('/api/fetch', methods=['POST'])
def api_fetch():
    with fetch_lock:
        global fetch_thread
        if fetch_thread and fetch_thread.is_alive():
            return jsonify({'status': 'busy', 'message': '抓取任务进行中'}), 409
        
        def fetch_worker():
            try:
                run_fetch()
                from config import load_config
                config = load_config()
                if config.get('auto_translate', True):
                    run_translate()
            except Exception as e:
                logger.error(f'抓取/翻译线程出错: {e}')
        
        fetch_thread = threading.Thread(target=fetch_worker, daemon=True)
        fetch_thread.start()
    
    return jsonify({'status': 'started'})

@app.route('/api/fetch/status', methods=['GET'])
def api_fetch_status():
    with fetch_lock:
        is_running = fetch_thread and fetch_thread.is_alive() if fetch_thread else False
    
    progress = get_fetch_progress()
    return jsonify({
        'running': is_running,
        **progress
    })

@app.route('/api/repos/<int:repo_id>/translate', methods=['POST'])
def api_translate(repo_id):
    with fetch_lock:
        global translate_thread
        if translate_thread and translate_thread.is_alive():
            return jsonify({'status': 'busy', 'message': '翻译任务进行中'}), 409
        
        def translate_worker():
            try:
                translate_single_repo(repo_id)
            except Exception as e:
                logger.error(f'翻译线程出错: {e}')
        
        translate_thread = threading.Thread(target=translate_worker, daemon=True)
        translate_thread.start()
    
    return jsonify({'status': 'started'})

@app.route('/api/translate/status', methods=['GET'])
def api_translate_status():
    with fetch_lock:
        is_running = translate_thread and translate_thread.is_alive() if translate_thread else False
    
    return jsonify({
        'running': is_running
    })

@app.route('/api/stats', methods=['GET'])
def api_stats():
    stats = get_stats()
    return jsonify(stats)


@app.route('/api/stats/detailed', methods=['GET'])
def api_stats_detailed():
    """返回详细统计数据（管理页用）"""
    stats = get_stats()
    return jsonify(stats)


@app.route('/api/topics', methods=['GET'])
def api_topics():
    """返回带频率统计的topics列表"""
    from db import get_all_topics as _get_all_topics
    topics = _get_all_topics()
    return jsonify({'topics': topics})


@app.route('/api/db/schema', methods=['GET'])
def api_db_schema():
    columns = get_db_schema()
    
    descriptions = {
        'id': ('自增主键', 'INTEGER'),
        'full_name': ('仓库全称 (owner/repo)', 'TEXT UNIQUE NOT NULL'),
        'description': ('仓库描述文字', 'TEXT'),
        'stars': ('星标数量', 'INTEGER DEFAULT 0'),
        'language': ('编程语言', 'TEXT'),
        'topics': ('话题标签，JSON数组', 'TEXT'),
        'html_url': ('GitHub 页面URL', 'TEXT'),
        'readme_path': ('README原文本地路径（绝对路径）', 'TEXT'),
        'readme_zh_path': ('README中文译文本地路径（绝对路径）', 'TEXT'),
        'translate_status': ('翻译状态: pending/done/error', 'TEXT DEFAULT pending'),
        'translate_error': ('翻译错误信息', 'TEXT'),
        'is_read': ('是否已读: 0=未读, 1=已读', 'INTEGER DEFAULT 0'),
        'keywords': ('触发抓取的关键词，JSON数组', 'TEXT'),
        'fetched_at': ('抓取时间', 'TEXT NOT NULL'),
        'updated_at': ('最后更新时间', 'TEXT NOT NULL'),
        'description_zh': ('仓库描述中文译文', 'TEXT'),
        'description_translate_status': ('Description翻译状态: pending/done/error', 'TEXT DEFAULT pending'),
    }
    
    result_columns = []
    for col in columns:
        desc_info = descriptions.get(col['name'], ('无说明', col['type']))
        result_columns.append({
            **col,
            'description': desc_info[0],
            'full_type': f"{desc_info[1] if not col['primary_key'] else ''}"
        })
    
    return jsonify({
        'table': 'repositories',
        'columns': result_columns,
    })


@app.route('/api/fetch/stop', methods=['POST'])
def api_fetch_stop():
    global fetch_thread, fetch_stop_flag
    with fetch_lock:
        import fetch as fetch_module
        fetch_module.fetch_stop = True
        if fetch_thread and fetch_thread.is_alive():
            fetch_thread.join(timeout=5)
        fetch_thread = None
    return jsonify({'status': 'stopped'})


@app.route('/api/description/translate', methods=['POST'])
def api_description_translate():
    global description_translate_thread
    
    with fetch_lock:
        if description_translate_thread and description_translate_thread.is_alive():
            return jsonify({'status': 'busy', 'message': '翻译任务进行中'}), 409
        
        def translate_worker():
            try:
                import translator
                from db import get_connection
                conn = get_connection()
                count_pending = conn.execute(
                    "SELECT COUNT(*) FROM repositories WHERE description_translate_status IN ('pending', 'error') AND description IS NOT NULL"
                ).fetchone()[0]
                conn.close()
                
                if count_pending == 0:
                    logger.info('没有待翻译的描述，任务结束')
                    return
                
                translator.run_translate_descriptions()
            except Exception as e:
                logger.error(f'描述翻译线程出错: {e}')
        
        description_translate_thread = threading.Thread(target=translate_worker, daemon=True)
        description_translate_thread.start()
    
    return jsonify({'status': 'started'})

@app.route('/api/description/translate/status', methods=['GET'])
def api_description_translate_status():
    global description_translate_thread
    
    with fetch_lock:
        is_running = description_translate_thread and description_translate_thread.is_alive() if description_translate_thread else False
    
    from translator import description_translate_current_repo
    from db import get_connection
    conn = get_connection()
    total = conn.execute('SELECT COUNT(*) FROM repositories').fetchone()[0]
    desc_done = conn.execute('SELECT COUNT(*) FROM repositories WHERE description_translate_status = ?', ('done',)).fetchone()[0]
    conn.close()
    
    return jsonify({
        'running': is_running,
        'total': total,
        'done': desc_done,
        'current_repo': description_translate_current_repo
    })

@app.route('/api/description/translate/stop', methods=['POST'])
def api_description_translate_stop():
    import translator
    translator.description_translate_stop = True
    return jsonify({'status': 'stopped'})

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
        formatted = ''.join(line.rstrip('\n') for line in tail)
        formatted = formatted.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        return jsonify({'logs': formatted})
    except FileNotFoundError:
        return jsonify({'logs': '日志文件不存在'})
    except Exception as e:
        return jsonify({'logs': f'读取失败: {e}'})

@app.route('/api/readme/translate', methods=['POST'])
def api_readme_translate():
    global translate_thread
    
    import translator as _translator
    _translator.readme_translate_stop = False
    
    with fetch_lock:
        if translate_thread and translate_thread.is_alive():
            return jsonify({'status': 'busy', 'message': '翻译任务进行中'}), 409
        
        def translate_worker():
            try:
                from translator import run_translate
                from db import get_connection
                conn = get_connection()
                pending_count = conn.execute(
                    "SELECT COUNT(*) FROM repositories WHERE translate_status IN ('pending', 'error')"
                ).fetchone()[0]
                conn.close()
                logger.info(f'README翻译: 找到 {pending_count} 个待处理仓库')
                
                if pending_count == 0:
                    logger.info('没有待翻译的 README，任务结束')
                    return
                
                run_translate(limit=pending_count, force=True)  # 手动触发时强制执行，无视 auto_translate 配置
            except Exception as e:
                logger.error(f'README 翻译线程出错: {e}')
        
        translate_thread = threading.Thread(target=translate_worker, daemon=True)
        translate_thread.start()
    
    return jsonify({'status': 'started'})


@app.route('/api/translate/stop', methods=['POST'])
def api_translate_stop():
    import translator
    global translate_thread
    with fetch_lock:
        translator.stop_readme_translate()
        translate_thread = None
    return jsonify({'status': 'stopped'})

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)