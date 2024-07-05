from flask import Flask, render_template

app = Flask("my-first-website")


@app.route("/")
def Osteotronik():
    return render_template("index.html")


@app.route("/productos")
def productos():
    return render_template("productos.html")


@app.route("/productos/clavos")
def clavos():
    return render_template("clavos.html")
