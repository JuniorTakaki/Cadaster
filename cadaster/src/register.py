
# Sistema de banco antigo, utilizando o SQL server.

# import sqlite3
# DB ="database.db"

# def conn_db():
#     try:
#         conn = sqlite3.connect('database.db')
#         print("Conexão com db foi estabelecido com sucesso")
#         return conn
#     except sqlite3.Error as err:
#         print(f"Erro ao conectar ao banco {err}")
#         return None
    
# def exec_query(query, params=()):
#     with sqlite3.connect('database.db') as conn:
#         cursor = conn.cursor()
#         cursor.execute(query, params)
#         conn.commit()

# def create_table_user():
#     query = (
#         "CREATE TABLE IF NOT EXISTS users ("
#         "id INTEGER PRIMARY KEY AUTOINCREMENT, "
#         "name TEXT NOT NULL, "
#         "surname TEXT NOT NULL, "
#         "year INTEGER NOT NULL"
#         ");"
#     )
#     exec_query(query)

# def save_db_user(name, surname, year):
#     from register import exec_query
#     query = "INSERT INTO users (name, surname, year) VALUES (?, ?, ?)"
#     params = (name, surname, year)
#     exec_query(query, params)
#     print(f'Usuário {name} cadastro.')

# def create_table_car():
#     query = (
#         "CREATE TABLE IF NOT EXISTS cars ("
#         "id INTEGER PRIMARY KEY AUTOINCREMENT, "
#         "brand TEXT NOT NULL, "
#         "model TEXT NOT NULL, "
#         "car_year INTEGER NOT NULL,"
#         "car_color TEXT NOT NULL"
#         ");"
#     )
#     exec_query(query)

# def save_db_car(brand, model, car_year, car_color):
#     from register import exec_query
#     query = "INSERT INTO cars (brand, model, car_year, car_color) VALUES (?, ?, ?, ?)"
#     params = (brand, model, car_year, car_color)
#     exec_query(query, params)
#     print(f'{brand} {model} cadastro.')
