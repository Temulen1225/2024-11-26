from flask import Flask, request

app = Flask(__name__)

# サーバールートへアクセスがあった時 --- (*1)
@app.route('/')
def index():
    # フォームを表示する --- (*2)
    return """
        <html><body>
        <form action="/hello" method="GET">
          名前: <input type="text" name="name">
          <br>
          ひとこと: <input type="text" name="comment">
          <br>
          <input type="submit" value="送信">
        </form>
        </body></html>
    """

# /hello へアクセスがあった時 --- (*3)
@app.route('/hello')
def hello():
    # nameのパラメータを得る --- (*4)
    name = request.args.get('name', '名無し')
    comment = request.args.get('comment', 'コメント無し')
    # 自己紹介を自動作成
    return """
        <html><body>
        <h1>{0}さん、こんにちは！</h1>
        <p>ひとこと：{1}</p>
        </body></html>
    """.format(name, comment)

if __name__ == '__main__':
    app.run(host='0.0.0.0')