from domain.models.user import User
from src.domain.service.user_service import create_table_user,save_db_user


def workflow():
    teste = User()
    teste.validate_name()
    teste.validate_email()
    save_db_user(teste.name, teste.email)

def main():
    create_table_user()
    workflow()

if __name__ == "__main__":
    main()