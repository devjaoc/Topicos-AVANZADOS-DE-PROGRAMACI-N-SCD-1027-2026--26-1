# core/logger.py
import logging
from logging.handlers import RotatingFileHandler
import os

if not os.path.exists("logs"):
    os.mkdir("logs")

def get_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    handler = RotatingFileHandler(
        "logs/app.log",
        maxBytes=200000,   # 200 KB
        backupCount=3,     # app.log.1, app.log.2...
        encoding="utf-8",
        delay=True          # MUY IMPORTANTE: solo abre el archivo cuando lo necesita
    )

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    return logger

logger = get_logger()