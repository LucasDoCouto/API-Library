import mysql.connector

def conectardb():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="livros"
    )
