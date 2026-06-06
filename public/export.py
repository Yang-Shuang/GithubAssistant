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

# 添加项目根目录到Python路径（用于导入config模块）
# public/ 的父级是 GithubAssistant（项目根目录）
PUBLIC_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.normpath(os.path.join(PUBLIC_DIR, '..'))

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)


def export_data():
    """导出数据库和README文件到public/data/目录"""
    
    # 加载配置以获取路径信息
    sys.path.insert(0, PROJECT_ROOT)
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
    
    # 扫描data/readme/目录，建立文件名到full_name的映射（修复数据库readme_path丢失的问题）
    print('🔍 扫描本地README文件...')
    readme_files = [f for f in os.listdir(readme_src_dir) if f.endswith('.md')]
    
    # 构建 full_name -> (filename, is_zh) 的映射
    filename_to_repo = {}
    for filename in readme_files:
        parts = filename.replace('.md', '').split('__')
        if len(parts) >= 2:
            full_name = '/'.join(parts[:-1]) if len(parts) > 2 else f'{parts[0]}/{parts[-1]}'
            is_zh = '_zh.md' in filename or (filename.endswith('.md') and '__' in filename and parts[-1].lower().endswith('_zh'))
            # 更简单的判断：文件名包含_zh_的认为是中文译文
            if '_zh_' in filename.lower() or filename.lower().endswith('_zh.md'):
                is_zh = True
            else:
                is_zh = False
            
            key = full_name.lower()
            if key not in filename_to_repo:
                filename_to_repo[key] = []
            filename_to_repo[key].append((filename, is_zh))
    
    print(f'📦 找到 {len(readme_files)} 个README文件，关联到 {len(filename_to_repo)} 个仓库')
    
    try:
        rows = cursor.execute('''
            SELECT id, full_name, description, stars, language, 
                   topics, html_url, readme_path, readme_zh_path, 
                   fetched_at, description_zh
            FROM repositories 
            ORDER BY id DESC
        ''').fetchall()
        
        print(f'📦 找到 {len(rows)} 条记录')
        
        for row in rows:
            repo_id, full_name, description, stars, language, topics_json, html_url, readme_path, readme_zh_path, fetched_at, description_zh = row
            
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
            
            # 构建相对路径（优先使用数据库中的路径，回退到本地文件扫描）
            relative_readme_path = None
            relative_readme_zh_path = None
            
            repo_key = full_name.lower()
            file_mapping = filename_to_repo.get(repo_key, [])
            
            if readme_path:
                try:
                    # 提取文件名（兼容Windows和Linux路径分隔符）
                    filename = readme_path.replace('\\', '/').split('/')[-1]
                    
                    relative_readme_path = f'data/readmes/{filename}'
                    
                    # 复制文件到readmes目录（避免重复）
                    dst_file = os.path.join(readmes_dst_dir, filename)
                    if not os.path.exists(dst_file):
                        shutil.copy2(os.path.join(readme_src_dir, filename), dst_file)
                except Exception as e:
                    print(f'⚠️ 警告：处理README失败 {full_name}: {e}')
            
            # 如果数据库中没有readme_path，从本地文件映射中查找
            if not relative_readme_path and file_mapping:
                for filename, is_zh in file_mapping:
                    if not is_zh:
                        relative_readme_path = f'data/readmes/{filename}'
                        dst_file = os.path.join(readmes_dst_dir, filename)
                        if not os.path.exists(dst_file):
                            shutil.copy2(os.path.join(readme_src_dir, filename), dst_file)
                        break
            
            if readme_zh_path:
                try:
                    # 提取文件名（兼容Windows和Linux路径分隔符）
                    filename = readme_zh_path.replace('\\', '/').split('/')[-1]
                    
                    relative_readme_zh_path = f'data/readmes/{filename}'
                    
                    dst_file = os.path.join(readmes_dst_dir, filename)
                    if not os.path.exists(dst_file):
                        shutil.copy2(os.path.join(readme_src_dir, filename), dst_file)
                except Exception as e:
                    print(f'⚠️ 警告：处理中文README失败 {full_name}: {e}')
            
            # 如果数据库中没有readme_zh_path，从本地文件映射中查找
            if not relative_readme_zh_path and file_mapping:
                for filename, is_zh in file_mapping:
                    if is_zh:
                        relative_readme_zh_path = f'data/readmes/{filename}'
                        dst_file = os.path.join(readmes_dst_dir, filename)
                        if not os.path.exists(dst_file):
                            shutil.copy2(os.path.join(readme_src_dir, filename), dst_file)
                        break
            
            # 构建仓库数据对象
            repo = {
                'id': repo_id,
                'full_name': full_name,
                'description': description or '',
                'description_zh': description_zh or '',
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
