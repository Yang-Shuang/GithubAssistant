import logging
import os
from datetime import datetime


def setup_logger(name='fetch'):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    log_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', f'{name}.log')
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    
    handler = logging.FileHandler(log_path, encoding='utf-8')
    handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(handler)
    
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(ColorFormatter())
    logger.addHandler(console_handler)
    
    return logger


def format_iso(dt=None):
    if dt is None:
        dt = datetime.now()
    return dt.isoformat()


def repo_to_filename(full_name):
    parts = full_name.replace('/', '__')
    return f"{parts}.md"


def repo_to_filename_zh(full_name):
    return f"{repo_to_filename(full_name).replace('.md', '_zh.md')}"


def get_readme_dir():
    data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'readme')
    os.makedirs(data_dir, exist_ok=True)
    return data_dir


# === ANSI 彩色日志支持 ===

class ColorFormatter(logging.Formatter):
    """支持终端 ANSI 颜色的日志格式化器"""

    COLORS = {
        'INFO': '\033[92m',      # 绿色 - 正常信息
        'WARNING': '\033[93m',   # 黄色 - 警告/进度  
        'ERROR': '\033[91m',     # 红色 - 错误
    }

    def __init__(self, fmt=None):
        if fmt is None:
            fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        super().__init__(fmt)
    
    def format(self, record):
        if hasattr(record, '_colored') and record._colored:
            color = getattr(record, '_color_code', '')
            reset = '\033[0m'
            msg = super().format(record)
            return f"{color}{msg}{reset}"
        elif record.levelname in self.COLORS:
            # 普通日志也着色（绿色=info，黄色=warning，红色=error）
            color = self.COLORS.get(record.levelname, '')
            reset = '\033[0m'
            msg = super().format(record)
            return f"{color}{msg}{reset}" if color else msg
        else:
            return super().format(record)


def log_done(logger, done_count, remaining, total, name='任务'):
    """输出完成进度日志（绿色高亮）"""  
    msg = f'[{name}] ✅ 已完成: {done_count} | 剩余: {remaining} | 总数: {total}'
    
    # 创建带颜色的记录
    record = logger.makeRecord(
        logger.name, 
        logging.INFO, 
        '', 
        0, 
        msg, 
        None, 
        None, 
        None, 
        None
    )
    setattr(record, '_colored', True)
    setattr(record, '_color_code', '\033[92m')  # 绿色
    
    logger.handle(record)


def log_stop(logger, done_count, total, name='任务'):
    """输出中断进度日志（红色高亮）"""  
    msg = f'[{name}] ⛔ 已停止: 已完成 {done_count}/{total}'
    
    record = logger.makeRecord(
        logger.name, 
        logging.WARNING, 
        '', 
        0, 
        msg, 
        None, 
        None, 
        None, 
        None
    )
    setattr(record, '_colored', True)
    setattr(record, '_color_code', '\033[91m')  # 红色
    
    logger.handle(record)

def log_skip(logger, name='任务'):
    """输出跳过日志（蓝色高亮）"""  
    msg = f'⏭️ 已跳过: {name}'
    
    record = logger.makeRecord(
        logger.name, 
        logging.INFO, 
        '', 
        0, 
        msg, 
        None, 
        None, 
        None, 
        None
    )
    setattr(record, '_colored', True)
    setattr(record, '_color_code', '\033[94m')  # 蓝色
    
    logger.handle(record)
