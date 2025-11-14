import sqlite3

def conectar_db():
    try:
        con = sqlite3.connect('produto.db')
        return con
    except sqlite3.Error as erro:
        return None