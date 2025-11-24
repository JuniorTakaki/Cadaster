import pyodbc
from typing import Optional, Tuple, Any

# --- CONFIGURAÇÕES SQL SERVER (AJUSTE AQUI) ---
SERVER = '127.0.0.1,1433'
DATABASE = 'master' 
USERNAME = 'sa'
PASSWORD = 'MoleDoy2025' # Sua senha atual
DRIVER = '{ODBC Driver 17 for SQL Server}' # O driver correto é CRÍTICO!

CONNECTION_STRING = (
    f'DRIVER={DRIVER};'
    f'SERVER={SERVER};'
    f'DATABASE={DATABASE};'
    f'UID={USERNAME};'
    f'PWD={PASSWORD};'
)

def conn_db() -> Optional[pyodbc.Connection]:
    try:
        conn = pyodbc.connect(CONNECTION_STRING)
        # print("Conexão com SQL Server estabelecida com sucesso!")
        return conn
    except pyodbc.Error as err:
        print(f"Erro ao conectar ao banco SQL Server: {err}")
        return None

def exec_query(query: str, params: Tuple[Any, ...] = ()):
    """Executa consultas de escrita (CREATE, INSERT, UPDATE, DELETE)."""
    conn = conn_db()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            cursor.close()
        except pyodbc.Error as err:
            print(f"Erro ao executar query: {err}")
        finally:
            conn.close()

def create_table_user():
    query = (
        "IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'users') "
        "CREATE TABLE users ("
        "id INT IDENTITY(1,1) PRIMARY KEY, "
        "name VARCHAR(255) NOT NULL, "
        "surname VARCHAR(255) NOT NULL, "
        "year INT NOT NULL"
        ");"
    )
    exec_query(query)

def save_db_user(name: str, surname: str, year: int):
    query = "INSERT INTO users (name, surname, year) VALUES (?, ?, ?)"
    params = (name, surname, year)
    exec_query(query, params)
    print(f'Usuário {name} cadastrado.')

def create_table_car():
    query = (
        "IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'cars') "
        "CREATE TABLE cars ("
        "id INT IDENTITY(1,1) PRIMARY KEY, "
        "brand VARCHAR(255) NOT NULL, "
        "model VARCHAR(255) NOT NULL, "
        "car_year INT NOT NULL,"
        "car_color VARCHAR(50) NOT NULL"
        ");"
    )
    exec_query(query)

def save_db_car(brand: str, model: str, car_year: int, car_color: str):
    query = "INSERT INTO cars (brand, model, car_year, car_color) VALUES (?, ?, ?, ?)"
    params = (brand, model, car_year, car_color)
    exec_query(query, params)
    print(f'{brand} {model} cadastrado.')

