import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>こんにちは！Flaskで作るWebサイトへようこそ。</h1>"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Render用にPORTを環境変数から取得
    app.run(host="0.0.0.0", port=port)  # 0.0.0.0にバインド

