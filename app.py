from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello"

@app.errorhandler(404)
def not_found(e):
    return "Page not found", 404
