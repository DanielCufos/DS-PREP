from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/Hasta_luego")
def hasta_luego():
    return "<p>Hasta Luego!</p>"

@app.route("/Buenas_tardes")
def buenas_tardes():
    return "<p>Buenas Tardes!</p>"

