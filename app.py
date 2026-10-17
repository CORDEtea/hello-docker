from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def hello():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"<h1>Hello, Docker!</h1><p>Текущее время: {now}</p>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
