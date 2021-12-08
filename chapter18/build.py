from flask import Flask
from jinja2.utils import F

#pip コマンドをcmdに打ち込みほしいパッケージをインストールできる。
#pip install [インストールしたいパッケージ]
#このインストールしたいパッケージはPyPIから探すことができる。
#そして、上記from flask import Flaskのようにインポートすることで機能を使用することができる
#今回importしたものはwebサーバーのプログラムを書く手助けをしてくれるプログラム

app = Flask(__name__)
@app.route('/')
def index():
    return "Hello, World!"

app.run(port=8000)