from flask import Flask, jsonify, request

from conectardb import conectardb

app = Flask(__name__)

# Lê o banco de dados

# Função de consultar todos os livros do banco de dados

@app.route('/livros')
def ler_livros():
    db_connection = conectardb()

    cursor = db_connection.cursor()

    cursor.execute("SELECT * FROM livros")
    livros = cursor.fetchall()
    
    livros_json = [dict(zip(cursor.column_names, livro)) for livro in livros]

    cursor.close()
    db_connection.close()

    return jsonify(livros_json)


# Função de consultar livros específicos
@app.route('/livros/<int:idconsulta>', methods=['GET'])
def ler_livro_id(idconsulta):
    db_connection = conectardb()

    cursor = db_connection.cursor()
    consultasql = "SELECT * FROM livros WHERE ID = '{}'" .format(idconsulta)
    cursor.execute(consultasql)
    livros = cursor.fetchall()
    
    livroid_json = [dict(zip(cursor.column_names, livro)) for livro in livros]

    cursor.close()
    db_connection.close()

    return jsonify(livroid_json)
# Função de editar livros

# Função de Excluir livros

# Função de Alocar livros

app.run(port=5000, host='localhost', debug=True)