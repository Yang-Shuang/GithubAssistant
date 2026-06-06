"""
clear.py - GitHub Reader 数据清理工具

用法：
    python clear.py              # 预览模式（默认）
    python clear.py --execute    # 执行删除操作

安全设计：
- 默认只查询不删除，显示即将操作的记录列表
- 需要显式传入 --execute 才真正执行删除
"""

import sys
import os
from config import load_config, get_db_path, get_readme_dir
from utils import setup_logger, repo_to_filename, repo_to_filename_zh

logger = setup_logger('clear')


def query_low_stars_repos(min_stars=1000):
    """查询 stars < min_stars 的仓库记录"""
    import sqlite3
    
    db_path = get_db_path()
    conn = sqlite3.connect(db_path)
    cursor = conn.execute(
        '''SELECT id, full_name, description, stars, language 
           FROM repositories 
           WHERE stars < ? OR stars IS NULL
           ORDER BY stars ASC''',
        (min_stars,)
    )
    
    repos = []
    for row in cursor:
        repo_id, full_name, desc, stars, lang = row
        
        # 查找 readme 文件（包括 .md 和 _zh.md）
        md_files = []
        try:
            # 生成标准文件名
            std_filename = repo_to_filename(full_name)
            zh_filename = repo_to_filename_zh(full_name)
            
            readme_dir = get_readme_dir()
            
            # 精确匹配这两个文件
            for expected_file in [std_filename, zh_filename]:
                filepath = os.path.join(readme_dir, expected_file)
                if os.path.exists(filepath):
                    md_files.append(filepath)
        except Exception as e:
            logger.warning(f'扫描 readme 目录失败 ({full_name}): {e}')
        
        repos.append({
            'id': repo_id,
            'full_name': full_name,
            'stars': stars if stars else 0,
            'readme_files': md_files,
        })
    
    conn.close()
    return repos


def delete_repos(repos):
    """删除仓库记录和相关文件"""
    import sqlite3
    
    db_path = get_db_path()
    
    for repo in repos:
        full_name = repo['full_name']
        
        # 删除数据库记录
        conn = sqlite3.connect(db_path)
        conn.execute('DELETE FROM repositories WHERE id = ?', (repo['id'],))
        conn.commit()
        conn.close()
        logger.info(f'已删除: {full_name} (stars={repo["stars"]})')
        
        # 删除 readme 文件
        for md_file in repo.get('readme_files', []):
            if os.path.exists(md_file):
                os.remove(md_file)
                logger.info(f'已删除文件: {md_file}')


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='GitHub Reader 数据清理工具')
    parser.add_argument(
        '--execute', 
        action='store_true', 
        help='执行删除操作（默认只预览）'
    )
    
    args = parser.parse_args()
    
    # 加载配置
    config = load_config()
    clear_limit_count = config.get('clear_limit_count', 2000)
    
    logger.info(f'清理阈值: stars < {clear_limit_count}')
    
    if not args.execute:
        print('=' * 60)
        print('预览模式 - 即将删除以下记录:')
        print('=' * 60)
        
        repos = query_low_stars_repos(clear_limit_count)
        
        if not repos:
            print('没有需要清理的记录')
            return
        
        total_files = sum(len(r.get('readme_files', [])) for r in repos)
        
        print(f'\n总计: {len(repos)} 条记录, {total_files} 个文件\n')
        print('-' * 60)
        
        # 显示前20条预览
        display_count = min(20, len(repos))
        for repo in repos[:display_count]:
            stars_str = str(repo['stars']) if repo['stars'] else 'N/A'
            files_info = f', {len(repo.get("readme_files", []))} 个文件' if repo.get('readme_files') else ''
            print(f'{repo["full_name"]} (stars={stars_str}){files_info}')
        
        if len(repos) > 20:
            print(f'... 还有 {len(repos) - 20} 条记录未显示\n')
        
        print('=' * 60)
        print('确认无误后，运行 python clear.py --execute 执行删除操作')
        print('=' * 60)
    else:
        print('=' * 60)
        print('执行模式 - 正在删除数据...')
        print('=' * 60)
        
        repos = query_low_stars_repos(clear_limit_count)
        
        if not repos:
            print('没有需要清理的记录')
            return
        
        total_files = sum(len(r.get('readme_files', [])) for r in repos)
        
        print(f'总计: {len(repos)} 条记录, {total_files} 个文件')
        
        # 二次确认
        confirm = input('\n确定要删除这些记录吗？(yes/no): ')
        if confirm.lower() != 'yes':
            print('操作已取消')
            return
        
        delete_repos(repos)
        
        print(f'\n清理完成: {len(repos)} 条记录, {total_files} 个文件')


if __name__ == '__main__':
    main()
