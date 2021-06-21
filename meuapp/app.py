from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from conection import *
from funcoes import *
from conf import *

app  = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/teste'

@app.route("/index")
def index():
    cur.execute('SELECT * FROM usuarios')
    dadosBD = cur.fetchall()

    return render_template("index.html", dados = dadosBD)

if __name__ == "__main__":
    app.run(debug=True)