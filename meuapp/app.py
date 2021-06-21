from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from conection import *
from funcoes import *
from conf import *

app  = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/teste'


@app.route("index")
def index():
    return render_template("index.html")
"""
try:
    #cur.execute("INSERT INTO usuarios(id, nome, idade) VALUES(1, 'Matheus', 23)")
    #cur.execute("INSERT INTO usuarios(id, nome, idade) VALUES(2, 'Ana', 23)")
    consulta()
    #print("inserção feita com sucesso!")
    conn.commit()
    cur.close()
    conn.close()
except:
    print("Erro ao consultar a tabela")

"""
if __name__ == "__main__":
    app.run(debug=True)