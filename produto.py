import sqlite3

def conectar_db():
    try:
        conectar = sqlite3.connect('produto.db')
        print("Conexão com db foi estabelecido com sucesso")
        return conectar
    except sqlite3.Error as erro:
        print(f"Erro ao conectar ao banco {erro}")
        return None
    
def executar_query(query, parametros=()):
    with sqlite3.connect('produto.db') as conexao:
        cursor = conexao.cursor()
        cursor.execute(query, parametros)
        conexao.commit()
