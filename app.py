from flask import Flask, url_for    
from markupsafe import escape
import sqlite3

app = Flask(__name__)

@app.route("/Hola")
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

@app.route('/')
def links():
    return f"""
    <a href="{url_for('hello_world')}">Hola</a>
    <div>
    <a href="{url_for('hasta_luego')}">Adios</a>
    <div>
    <a href="{url_for('buenas_tardes')}">Buenas</a>
    <div>
    <a href="{url_for('mostrar_perfil_usuario', username= 'Adrian')}">usuario</a>
    <div>
    <a href="{url_for('verificar_aprobacion', nota= '8')}">Verificar Nota</a>
"""
db = None


def dict_factory(cursor, row):
  """Arma un diccionario con los valores de la fila."""
  fields = [column[0] for column in cursor.description]
  return {key: value for key, value in zip(fields, row)}


def abrirConexion():
   global db
   db = sqlite3.connect("instance/datos.sqlite")
   db.row_factory = dict_factory


def cerrarConexion():
   global db
   db.close()
   db = None


@app.route("/test-db")
def testDB():
   abrirConexion()
   cursor = db.cursor()
   cursor.execute("SELECT COUNT(*) AS cant FROM usuarios; ")
   res = cursor.fetchone()
   registros = res["cant"]
   cerrarConexion()
   return f"Hay {registros} registros en la tabla usuarios"


@app.route("/datos-db")
def datosDB():
   abrirConexion()
   cursor = db.cursor()
   cursor.execute("SELECT usuario,email FROM usuarios; ")
   res = cursor.fetchone()
   email = res["email"]
   usuario = res["usuario"]

   cerrarConexion()
   return f"El mail de {usuario} es {email} en la db"