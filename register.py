import sqlite3
DB ="register.db"

def conn_db():
    try:
        conn = sqlite3.connect('register.db')
        print("Conexão com db foi estabelecido com sucesso")
        return conn
    except sqlite3.Error as err:
        print(f"Erro ao conectar ao banco {err}")
        return None
    
def exec_query(query, params=()):
    with sqlite3.connect('register.db') as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()

def create_table():
    query = (
        "CREATE TABLE IF NOT EXISTS register ("
        "id INTEGER PRIMARY KEY AUTOINCREMENT, "
        "name TEXT NOT NULL, "
        "surname TEXT NOT NULL, "
        "year INTEGER NOT NULL"
        ");"
    )
    exec_query(query)

def save_db(name, surname, year):
    from register import exec_query
    query = "INSERT INTO register (name, surname, year) VALUES (?, ?, ?)"
    params = (name, surname, year)
    exec_query(query, params)
    print(f'produto {name} salvo no banco com sucesso')
