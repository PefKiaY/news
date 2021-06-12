"""
程序的启动入口

加载配置文件：
1.数据库配置
2.redis配置
3.session配置
4.csrf配置
5.迁移
6.日志记录

"""
from info import create_app

app = create_app('develop')


@app.route('/')
def index():
    return '这是主页'


if __name__ == '__main__':
    app.run(debug=True)
