import logging
from logging.handlers import RotatingFileHandler

import redis
from flask import Flask
from flask.ext.session import Session
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.wtf import CSRFProtect

from config import config_dict

# 定义redis
redis_store = None
# 创建SQLAlchemy对象
db = SQLAlchemy()


def create_app(env_name):
    app = Flask(__name__)

    # 使用db,关联app
    db.init_app(app)

    # 加载配置信息
    config = config_dict[env_name]
    app.config.from_object(config)

    # 创建redis对象
    global redis_store
    redis_store = redis.StrictRedis(host=config.REDIS_HOST, port=config.REDIS_PORT, decode_responses=True)

    # 设置csrf对app进行保护
    CSRFProtect(app)

    # 初始化Session
    Session(app)

    return app


# 配置日志记录信息,就是为了方便记录程序运行过程
def log_file(LEVEL):
    # 设置日志的记录等级,大小关系: DEBUG<INFO<WARING<ERROR
    logging.basicConfig(level=LEVEL)  # 调试debug级
    # 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
    file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024 * 1024 * 100, backupCount=10)
    # 创建日志记录的格式 日志等级 输入日志信息的文件名 行数 日志信息
    formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
    # 为刚创建的日志记录器设置日志记录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志工具对象（flask app使用的）添加日志记录器
    logging.getLogger().addHandler(file_log_handler)
