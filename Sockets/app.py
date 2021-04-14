from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import gunicorn

app = Flask(__name__)

app.config["SECRET_KEY"] = "key momint"

socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/', methods = ["GET", "POST"])
def home():
    return render_template("index.html")

@socketio.on("connect", namespace="/test")
def test_connect():
    emit("my connection", {"data": "Connected"})

@socketio.on("my new message", namespace="/test")
def test_message(message):
    emit("new message", {"data": message["data"]})

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    socketio.run(app, host=HOST, port=PORT)

