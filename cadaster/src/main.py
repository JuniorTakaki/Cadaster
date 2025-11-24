from cadastre import Cadastre
from car import Car
from database import create_table_user, save_db_user, save_db_car,create_table_car

def user_workflow() -> None:
    user = Cadastre()
    user.user_name()
    user.user_surname()
    user.user_age()
    save_db_user(user.name, user.surname, user.age)
    
def car_workflow() -> None:
    car = Car()
    car.car_brand()
    car.car_model()
    car.car_year()
    car.car_color()
    save_db_car(car.brand, car.model, car.year, car.color)

def main():
    create_table_user()
    create_table_car()
    print("Escolha o fluxo:")
    print("1 - Cadastro de Usuário")
    print("2 - Cadastro de Carro")
    
    opc = input("Opção:")
    
    if opc == "1":
        user_workflow()
    else:
        car_workflow()

if __name__ == "__main__":
    main()
