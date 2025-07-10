import logging
from logging.handlers import RotatingFileHandler
import os

def configure_logging(name):
    # 获取环境变量中的 PROFILE，默认值为 dev 并转为小写
    profile = os.getenv("PROFILE", "dev").lower()
    # 定义日志格式
    formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")

    # 创建日志对象
    logger = logging.getLogger(name)

    if profile == "prod":
        logger.setLevel(logging.INFO)
        # 移除所有现有的处理器
        for handler in logger.handlers:
            logger.removeHandler(handler)
        # 创建文件处理器
        file_handler = RotatingFileHandler(
            "app.log",
            maxBytes=0,
            backupCount=20,
            encoding="utf-8")
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    else:
        # 开发环境配置
        logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
        logger.addHandler(logging.getLogger().handlers[0])

    return logger
