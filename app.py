from flask import Flask, jsonify, request

app = Flask(__name__)

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