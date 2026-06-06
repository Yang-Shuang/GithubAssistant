import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

USER_CONFIG_PATH = os.path.join(BASE_DIR, 'user-config.json')
DEFAULT_CONFIG_PATH = os.path.join(BASE_DIR, 'config.json')


def load_config():
    config_path = USER_CONFIG_PATH if os.path.exists(USER_CONFIG_PATH) else DEFAULT_CONFIG_PATH
    with open(config_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def get_data_dir():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')

def get_readme_dir():
    readme_dir = os.path.join(get_data_dir(), 'readme')
    os.makedirs(readme_dir, exist_ok=True)
    return readme_dir

def get_db_path():
    db_path = os.path.join(get_data_dir(), 'db.sqlite')
    os.makedirs(get_data_dir(), exist_ok=True)
    return db_path


KW_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'keywords.json')

def load_keywords():
    """从 keywords.json 加载关键词列表，返回 key 值数组"""
    with open(KW_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return [kw['key'] for kw in data.get('keywords', [])]
