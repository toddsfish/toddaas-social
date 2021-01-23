from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "index"

@app.route("/upload")
def hello():
    return "Hello World!"