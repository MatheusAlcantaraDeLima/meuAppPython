from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from conection import *
from funcoes import *
from conf import *

app  = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/teste'

@app.route("/index")
def index():
    dados = consulta()

    return render_template("index.html", pessoa = dados)

if __name__ == "__main__":
    app.run(debug=True)