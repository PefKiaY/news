from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from config import Config

def create_app():
    app = Flask(__name__)

    # 创建数据库对象，关联app
    db = SQLAlchemy(app)
    # 加载配置信息
    app.config.from_object(Config)
