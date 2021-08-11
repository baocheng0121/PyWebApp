import configparser
from flask import *
import type
from werkzeug.utils import redirect


app = Flask(__name__)


session = {'logged_in': False}        # 状态存储 str->bool


@app.route('/')
def home():
    """
    Home Page
    """
    if not session['logged_in']:
        return redirect(url_for('login'))


@app.route('/login')
def login():
    """
        main screen
    """
    return render_template('login.html')


@app.route('/logout')
def logout():
    """
    log out
    """
    return redirect(url_for("home"))


if __name__ == '__main__':
    # 根据config文件获取端口号
    config = configparser.ConfigParser()
    config.read('config.ini')
    if 'port' not in config['SETUP']:
        config['SETUP']['port'] = type.DEFAULT_PORT
    print("="*80)
    print("""项目:   Flask项目模板
    作者:   王保成
    时间:   2021-08-10 19:16
    IP:     127.0.0.1
    端口:   {}""".format(config['SETUP']['port']))
    print("="*80)
    app.run()

