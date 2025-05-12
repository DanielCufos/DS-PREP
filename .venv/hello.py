from flask import Flask
from markupsafe import escape

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


@app.route('/usuario/<username>')
def mostrar_perfil_usuario(username):
    return f'Usuario {escape(username)}'

@app.route('/verificar-aprobacion/<int:nota>')
def verificar_aprobacion(nota):
    if nota >= 7:
        return "Aprobado"
    else: 
        return "Desaprobado"

@app.route('/path/<path:subpath>')
def mostrar_subpath(subpath):
    return f'Subpath {escape(subpath)}'

@app.route('/sumar/<int:numero>/<int:numero2>')
def suma(numero, numero2):
    resultado = numero + numero2
    return f'Resultado = {(resultado)}'

