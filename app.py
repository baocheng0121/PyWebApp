import configparser
from flask import *
import types
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


@app.route('/login', methods=['POST', 'GET'])
def login():
    """
        main screen
    """
    if request.method == 'POST':
        pass

    elif request.method == 'GET':
        pass

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
    if 'port' not in config['SETUP'] or type(eval(config['SETUP']['port'])) != int:
        config['SETUP']['port'] = types.DEFAULT_PORT
    port = int(config['SETUP']['port'])
    print("="*80)
    print("""项目:   Flask项目模板
    作者:   王保成
    时间:   2021-08-10 19:16
    IP:     127.0.0.1
    端口:   {}""".format(config['SETUP']['port']))
    print("="*80)
    app.run(debug=True, port=port)

