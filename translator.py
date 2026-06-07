import requests
import os
from config import load_config
from utils import setup_logger, get_readme_dir, repo_to_filename, repo_to_filename_zh
from db import init_db, get_pending_translates, update_translate_status, get_connection

logger = setup_logger('translator')

description_translate_stop = False
description_translate_current_repo = None


TRANSLATE_PROMPT = """你是一名技术文档翻译专家，请将以下 README 翻译为简体中文。

## 翻译前检查

先判断原文语言：
- 如果原文已经是简体中文，或中文内容超过 80%，直接输出原文，不做任何修改
- 否则按以下规则翻译

**保持原文不翻译的内容：**
- 产品名、工具名：OpenCode、Claude Code、Cursor、VS Code、Android Studio、WSL 等
- 命令行命令及参数：`opencode`、`--log-level`、`/new` 等
- 配置字段名：`prompt`、`permission`、`default_agent`、`mode` 等
- 文件名及路径：`AGENTS.md`、`opencode.json`、`~/.config/opencode/` 等
- 代码块（``` 包裹的内容）：完整保留，一字不改
- 技术术语缩写：API、CLI、TUI、MCP、WSL、LLM 等
- 模型名称：Qwen3、Claude、GPT、Gemini 等
- agent 名称：build、plan、general 等

**翻译时注意：**
- 技术名词首次出现时可在括号内保留英文原文，例如：权限（permission）
- 保持 Markdown 格式结构不变，标题层级、列表、代码块格式原样保留
- 语言风格简洁自然，避免机械直译，符合中文技术文档习惯
- "you" 译为"你"，不用"您"

## 待翻译内容如下

{content}"""

def call_llm(text, max_retries=3):
    config = load_config()
    llama_config = config.get('llama_cpp', {})
    base_url = llama_config.get('base_url', 'http://localhost:8080')
    model = llama_config.get('model', 'qwen3.6-35b-a3b')
    
    url = base_url.rstrip('/') + '/v1/chat/completions'
    headers = {'Content-Type': 'application/json'}
    data = {
        'model': model,
        'messages': [
            {'role': 'system', 'content': 'You are a helpful assistant.'},
            {'role': 'user', 'content': TRANSLATE_PROMPT.format(content=text)}
        ],
        'temperature': 0.3,
        'max_tokens': config.get('llama_cpp', {}).get('max_tokens', 4096)
    }
    
    timeout_sec = llama_config.get('timeout', 3600)  # 默认60分钟，支持大文件翻译
    
    for attempt in range(max_retries):
        try:
            logger.info(f'翻译请求 (第 {attempt + 1}/{max_retries} 次尝试)...')
            response = requests.post(url, headers=headers, json=data, timeout=timeout_sec)
            response.raise_for_status()
            result = response.json()
            content = result['choices'][0]['message'].get('content', '')
            if not content:
                reasoning = result['choices'][0]['message'].get('reasoning_content', '')
                if reasoning:
                    logger.info('检测到推理模型，使用 reasoning_content 作为翻译结果')
                    return reasoning
            return content
        except Exception as e:
            logger.warning(f'翻译请求失败 (第 {attempt + 1}/{max_retries} 次): {e}')
            if attempt < max_retries - 1:
                import time
                wait_time = 30 * (attempt + 1)
                logger.info(f'等待 {wait_time} 秒后重试...')
                time.sleep(wait_time)
            else:
                logger.error(f'翻译调用最终失败: {e}')
                raise

def translate_readme(text):
    return call_llm(text)

def translate_description(description):
    """翻译仓库描述信息为中文，复用 TRANSLATE_PROMPT"""
    return call_llm(description)

def translate_single_repo(repo_id):
    config = load_config()
    init_db()
    
    repo = get_repo(repo_id)
    if not repo:
        logger.error(f'仓库 {repo_id} 不存在')
        return False
    
    full_name = repo['full_name']
    readme_dir = get_readme_dir()
    
    if not repo.get('readme_path'):
        logger.warning(f'{full_name} 没有 README 文件，跳过')
        return False
    
    try:
        full_readme_path = os.path.join(readme_dir, repo['readme_path'])
        with open(full_readme_path, 'r', encoding='utf-8') as f:
            readme_content = f.read()
        
        logger.info(f'正在翻译 {full_name}')
        
        translated = translate_readme(readme_content)
        
        zh_filename = repo_to_filename_zh(full_name)
        zh_filepath = os.path.join(readme_dir, zh_filename)
        
        with open(zh_filepath, 'w', encoding='utf-8') as f:
            f.write(translated)
        
        update_translate_status(repo_id, 'done', readme_zh_path=zh_filename)
        logger.info(f'{full_name} 翻译完成')
        return True
        
    except Exception as e:
        error_msg = str(e)
        logger.error(f'{full_name} 翻译失败: {error_msg}')
        return False

def get_repo(repo_id):
    from db import get_repo as _get_repo
    return _get_repo(repo_id)

def run_translate(limit=10, force=False):
    global readme_translate_stop
    
    # === 每次启动时重置中断标志 ===
    readme_translate_stop = False
    
    config = load_config()
    auto_translate = config.get('auto_translate', True)
    
    if not auto_translate and not force:
        logger.info('自动翻译已关闭，跳过批量翻译')
        return
    
    init_db()
    
    readme_dir = get_readme_dir()
    repos = get_pending_translates(limit)
    
    total_count = len(repos)
    done = 0
    
    if not repos:
        logger.info('没有待翻译的 README')
        return
    
    logger.info(f'开始翻译 {total_count} 个 README')
    
    for repo in repos:
        # === 中断检查（每个repo前）===
        if readme_translate_stop:
            from utils import log_stop
            log_stop(logger, done, total_count, 'README翻译')
            return
        
        repo_id = repo['id']
        full_name = repo['full_name']
        
        if not repo.get('readme_path'):
            logger.warning(f'{full_name} 没有 README 文件，跳过')
            continue
        
        try:
            full_readme_path = os.path.join(readme_dir, repo['readme_path'])
            with open(full_readme_path, 'r', encoding='utf-8') as f:
                readme_content = f.read()
            
            logger.info(f'正在翻译 {full_name}')
            
            translated = translate_readme(readme_content)
            
            zh_filename = repo_to_filename_zh(full_name)
            zh_filepath = os.path.join(readme_dir, zh_filename)
            
            with open(zh_filepath, 'w', encoding='utf-8') as f:
                f.write(translated)
            
            update_translate_status(repo_id, 'done', readme_zh_path=zh_filename)
            done += 1
            
            # === 进度日志（每完成一个）===
            from utils import log_done
            remaining = total_count - done
            log_done(logger, done, remaining, total_count, 'README翻译')
            
        except Exception as e:
            error_msg = str(e)
            logger.error(f'{full_name} 翻译失败: {error_msg}')

def translate_description_single(repo_id):
    """翻译单条仓库描述的中文"""
    init_db()
    
    repo = get_repo(repo_id)
    if not repo:
        logger.error(f'仓库 {repo_id} 不存在')
        return False
    
    full_name = repo['full_name']
    description = repo.get('description')
    
    if not description:
        logger.warning(f'{full_name} 没有描述信息，跳过')
        return False
    
    try:
        logger.info(f'正在翻译 {full_name} 的描述')
        
        translated = translate_description(description)
        
        conn = get_connection()
        conn.execute(
            'UPDATE repositories SET description_zh = ?, description_translate_status = ? WHERE id = ?',
            (translated, 'done', repo_id)
        )
        conn.commit()
        conn.close()
        
        logger.info(f'{full_name} 描述翻译完成')
        return True
        
    except Exception as e:
        error_msg = str(e)
        logger.error(f'{full_name} 描述翻译失败: {error_msg}')
        return False

def run_translate_descriptions():
    """批量翻译所有待翻译的仓库描述"""
    global description_translate_stop, description_translate_current_repo
    
    # === 每次启动时重置中断标志 ===
    description_translate_stop = False
    
    init_db()
    
    from db import get_connection, get_repo
    import json
    
    conn = get_connection()
    cursor = conn.execute(
        'SELECT * FROM repositories WHERE description_translate_status = ? AND description IS NOT NULL AND LENGTH(description) > 0 ORDER BY stars DESC NULLS LAST',
        ('pending',)
    )
    rows = cursor.fetchall()
    conn.close()
    
    repos = []
    for row in rows:
        repo = dict(row)
        repo['topics'] = json.loads(repo['topics']) if repo['topics'] else []
        repo['keywords'] = json.loads(repo['keywords']) if repo['keywords'] else []
        repos.append(repo)
    
    total = len(repos)
    done = 0
    
    if not repos:
        logger.info('没有待翻译的描述')
        return {'total': total, 'done': done, 'stopped': False}
    
    logger.info(f'开始翻译 {len(repos)} 个仓库描述')
    
    for repo in repos:
        if description_translate_stop:
            logger.info(f'描述翻译被中断，已翻译 {done}/{total}')
            description_translate_current_repo = None
            return {'total': total, 'done': done, 'stopped': True}
        
        repo_id = repo['id']
        full_name = repo['full_name']
        description_translate_current_repo = full_name
        
        try:
            logger.info(f'正在翻译 {full_name} 的描述')
            
            description = repo.get('description')
            translated = translate_description(description)
            
            conn = get_connection()
            conn.execute(
                'UPDATE repositories SET description_zh = ?, description_translate_status = ? WHERE id = ?',
                (translated, 'done', repo_id)
            )
            conn.commit()
            conn.close()
            
            done += 1
            logger.info(f'{full_name} 描述翻译完成')
            
        except Exception as e:
            error_msg = str(e)
            logger.error(f'{full_name} 描述翻译失败: {error_msg}')
        
        description_translate_current_repo = None
    
    description_translate_stop = False
    
    logger.info(f'描述翻译完成: 成功 {done}/{total}')
    description_translate_current_repo = None
    return {'total': total, 'done': done, 'stopped': False}


readme_translate_stop = False


def stop_readme_translate():
    """设置 README 翻译中断标志"""
    global readme_translate_stop
    readme_translate_stop = True


def is_readme_translating():
    """检查是否在翻译中（返回停止标志的相反值）"""
    return not readme_translate_stop

if __name__ == '__main__':
    run_translate()