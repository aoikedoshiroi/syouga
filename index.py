from flask import Flask, request, jsonify
import gradio as gr
from gradio.routes import App

# Flaskアプリのインスタンス作成
app = Flask(__name__)

# Gradioインターフェースの定義
def reverse_text(text):
    return text[::-1]

gr_interface = gr.Interface(fn=reverse_text, inputs="text", outputs="text")

# GradioをFlaskのルート "/gradio" にマウント
gr_app = App.create_app(gr_interface)
app.wsgi_app = gr_app

# カスタムAPIエンドポイント (任意で追加)
@app.route("/api/reverse", methods=["POST"])
def reverse_api():
    data = request.json.get("text", "")
    result = reverse_text(data)
    return jsonify({"reversed_text": result})

# Flaskアプリのメインエントリーポイント
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

