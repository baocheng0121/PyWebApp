import configparser
from flask import Flask

import type

app = Flask(__name__)


@app.route('/')
def hello_word():
    """
        网关心跳
    """
    print("Hello World")


if __name__ == '__main__':
    # 根据config文件获取端口号
    config = configparser.ConfigParser()
    config.read('config.ini')
    if 'port' not in config['SETUP']:
        config['SETUP']['port'] = type.DEFAULT_PORT
    print("="*70)
    print("""
    项目:   Flask项目模板
    作者:   王保成
    时间:   2021-08-10 19:16
    IP:     127.0.0.1
    端口:   {}
    """.format(config['SETUP']['port']))
    print("="*70)
    app.run()

