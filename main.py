#!/usr/bin/python3
from flask import Flask, render_template
import platform, os
import socket, subprocess

app = Flask(__name__)
mensaje=[]


@app.route("/")
def index():
    return render_template('index.html',mensaje=['HEMOS ANALIZADO SU ORDENADOR', 'pulse una opcion del menu de arriba',''])

@app.route("/<parametro>")
def mostrar(parametro):
    if parametro=="nombre":
        return render_template('index.html', mensaje=['Nombre del Equipo', socket.gethostname()])
    elif parametro=="direccion":
        return render_template('index.html', mensaje=['Dirección IP',socket.gethostbyname(socket.gethostname() + ".local")])
    elif parametro=="arquitectura":
        return render_template('index.html', mensaje=['Arquitectura', platform.architecture()])
    elif parametro=="reiniciar":
        return render_template('index.html', mensaje=['Reiniciar PC', subprocess.run("shutdown -r now", shell=True)])
    else:
        return render_template('index.html',mensaje=['Error','Parámetro no válido, haz clic en el menú superior'])

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)

