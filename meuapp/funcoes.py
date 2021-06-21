from conection import *
def consulta():
    cur.execute('SELECT * FROM usuarios')
    dadosBD = cur.fetchall()
    for i in dadosBD:
        print(i)

    
    #dados = cur.fetchone()
    #print(dados)
    #dados = cur.fetchone()
    #print(dados)