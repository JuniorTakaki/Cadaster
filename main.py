from cadastre import Cadastre
from register import create_table, save_db

def main():
    create_table()

    user = Cadastre()
    
    user.user_name()
    user.user_surname()
    user.user_year()
    save_db(user.name, user.surname, user.year)

if __name__ == "__main__":
    main()
