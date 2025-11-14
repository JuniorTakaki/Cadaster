import sqlite3
DB ="produto.db"

def conectar_db():
    try:
        conectar = sqlite3.connect('produto.db')
        print("Conexão com db foi estabelecido com sucesso")
        return conectar
    except sqlite3.Error as erro:
        print(f"Erro ao conectar ao banco {erro}")
        return None
    
def executar_query(busca, parametros=()):
    with sqlite3.connect('produto.db') as conexao:
        cursor = conexao.cursor()
        cursor.execute(busca, parametros)
        conexao.commit()

def criar_tabela():
    busca = (
        "CREATE TABLE IF NOT EXISTS produtos ("
        "id INTEGER PRIMARY KEY AUTOINCREMENT, "
        "nome TEXT NOT NULL, "
        "quantidade INTEGER NOT NULL, "
        "ano INTEGER NOT NULL"
        ");"
    )
    executar_query(busca)
    print("Tabela 'produtos' criada ou já existente.")

def salvar_no_banco(self):
    from produto import executar_query
    busca = "INSERT INTO produtos (nome, quantidade, ano) VALUES (?, ?, ?)"
    parametros = (self.nome, self.quantidade, self.ano)
    executar_query(busca, parametros)
    print(f'produto {self.nome} salvo no banco com sucesso')
