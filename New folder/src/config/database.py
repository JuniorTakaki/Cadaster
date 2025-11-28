import pyodbc
from typing import Optional, Tuple, Any

SERVER = '127.0.0.1,1433'
DATABASE = 'master' 
USERNAME = 'sa'
PASSWORD = 'MoleDoy2025'
DRIVER = '{ODBC Driver 17 for SQL Server}' 

CONNECTION_STRING = (
    f'DRIVER={DRIVER};'
    f'SERVER={SERVER};'
    f'DATABASE={DATABASE};'
    f'UID={USERNAME};'
    f'PWD={PASSWORD};'
)

def conn_db():
    try:
        conn = pyodbc.connect(CONNECTION_STRING)
        return conn
    except pyodbc.Error as err:
        print(f"não foi possivel conectar pelo erro {err}")
        return None
    
def fetch_query(query: str, params: Tuple[Any,...] = ()):
    conn = conn_db()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute(query, params)
            rows = cursor.fetchall()
            cursor.close()
            conn.close()
            return rows
        except pyodbc.Error as err:
            print(f"Erro ao executar SELECT: {err}")
            return None
    return None

def exec_query(query : str, params: Tuple[Any,...] = ()):
    conn = conn_db()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute(query,params)
            conn.commit()
            cursor.close()
        except pyodbc.Error as err:
            print(f"Erro ao executar query: {err}")
        finally:
            conn.close()