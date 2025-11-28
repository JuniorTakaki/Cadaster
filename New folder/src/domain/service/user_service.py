from src.config.database import exec_query,fetch_query
from typing import Optional

def create_table_user():
    query = (
        "IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'users') "
        "CREATE TABLE users ("
        "id INT IDENTITY(1,1) PRIMARY KEY,"
        "name VARCHAR(255) NOT NULL,"
        "email VARCHAR(255) UNIQUE NOT NULL"
        ");"
            )
    exec_query(query)

def save_db_user(name: str, email : str):
    query = "INSERT INTO users (name, email) VALUES (?,?)"
    params = (name, email)
    exec_query(query,params)
    print(f"Cadastrado")

def find_user_by_name(name: str) -> Optional[list]:
        query = "Select id, name, email FROM  users WHERE name = ? "
        params = (name,)
        return fetch_query(query,params)


def check_email_exists(email: str) -> bool:
   
    query = "SELECT COUNT(id) FROM users WHERE email = ?"
    params = (email,)
    
    result = fetch_query(query, params)
    
    if result and result[0][0] > 0:
        return True # Email já existe
    return False # Email não existe
