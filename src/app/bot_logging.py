# bot_logging.py
import logging.handlers
import os

LOG_DIR = 'bot_logs'
os.makedirs(LOG_DIR, exist_ok=True)

file_handler = logging.handlers.RotatingFileHandler(
    filename=os.path.join(LOG_DIR, 'discord.log'),
    encoding='utf-8',
    maxBytes=32 * 1024 * 1024,
    backupCount=5,
)

dt_fmt = '%Y-%m-%d %H:%M:%S'
formatter = logging.Formatter('[{asctime}] [{levelname:<8}] {name}: {message}', dt_fmt, style='{')
file_handler.setFormatter(formatter)
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
logger.addHandler(file_handler)


def getLogger():
    return logger
