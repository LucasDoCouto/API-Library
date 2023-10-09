from flask import Flask, jsonify, request

from conectardb import conectardb

app = Flask(__name__)


# Função de consultar todos os livros do banco de dados

@app.route('/livros/', methods=['GET'])
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
    consultasql = "SELECT * FROM livros WHERE ID = %s"
    cursor.execute(consultasql, (idconsulta,))
    livros = cursor.fetchall()
    
    livroid_json = [dict(zip(cursor.column_names, livro)) for livro in livros]

    cursor.close()
    db_connection.close()

    return jsonify(livroid_json)

# Função de editar livros

@app.route('/livros/<int:idedit>', methods=['PUT'])
def editar_livro_id(idedit):
    livro_json = request.get_json()

    db_connection = conectardb()

    cursor = db_connection.cursor()
    atualizasql = "UPDATE livros SET nome = %s WHERE id = %s;"
    cursor.execute(atualizasql, (livro_json['nome'], idedit,))
    db_connection.commit()
    consultasql = "SELECT * FROM livros WHERE ID = %s"
    cursor.execute(consultasql, (idedit,))
    livros = cursor.fetchall()
    
    livroid_json = [dict(zip(cursor.column_names, livro)) for livro in livros]

    cursor.close()
    db_connection.close()

    return jsonify(livroid_json)

# Função de incluir novos livros

@app.route('/livros/', methods=['POST'])
def adicionar_livro():
    novolivro_json = request.get_json()

    db_connection = conectardb()

    cursor = db_connection.cursor()

    insertsql = "INSERT INTO `livros`(`nome`) VALUES (%s)"
    cursor.execute(insertsql, (novolivro_json['nome'],))
    db_connection.commit()

    consultasql = "SELECT * FROM livros WHERE nome = %s"
    cursor.execute(consultasql, (novolivro_json['nome'],))
    livros = cursor.fetchall()
    
    livroid_json = [dict(zip(cursor.column_names, livro)) for livro in livros]

    cursor.close()
    db_connection.close()

    return jsonify(livroid_json)

# Função de Excluir livros
@app.route('/livros/<int:idremove>', methods=['DELETE'])
def remover_livro(idremove):
    db_connection = conectardb()

    cursor = db_connection.cursor()

    removesql = "DELETE FROM `livros` WHERE id = %s"
    cursor.execute(removesql, (idremove,))
    db_connection.commit()

    cursor.execute("SELECT * FROM livros")
    livros = cursor.fetchall()
    
    livros_json = [dict(zip(cursor.column_names, livro)) for livro in livros]

    cursor.close()
    db_connection.close()

    return jsonify(livros_json)


# Função de Alocar livros

app.run(port=8000, host='localhost', debug=True)