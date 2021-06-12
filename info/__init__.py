import redis
from flask import Flask
from flask.ext.session import Session
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.wtf import CSRFProtect

from config import config_dict

# 定义redis
redis_store = None


def create_app(env_name):
    app = Flask(__name__)

    # 创建数据库对象，关联app
    db = SQLAlchemy(app)
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
