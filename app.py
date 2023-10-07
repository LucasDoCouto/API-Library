from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'O Senhor dos Anéis -  A Sociedade do Anel',
        'autor': 'J. R. R, Tolkien',
        'quantidade': 5,
        'disponibilidade': 5
    },
    {
        'id': 2,
        'titulo': 'A Guerra dos Tronos',
        'autor': 'George R. R. Martin',
        'quantidade': 5,
        'disponibilidade': 5
    },
    {
        'id': 3,
        'titulo': 'Harry Potter e a câmara secreta',
        'autor': 'J. K. Rowling',
        'quantidade': 5,
        'disponibilidade': 5
    }
]

usuarios = [
    {
        'id': 1,
        'nome': 'Lucas'
    },
    {
        'id': 2,
        'nome': 'Carlos'
    }
]

# Função de consultar livros
@app.route('/livros')
def ler_livros():
    return jsonify(livros)

# Função de consultar livros específicos

# Função de editar livros

# Função de Excluir livros

# Função de Alocar livros

app.run(port=5000, host='localhost', debug=True)