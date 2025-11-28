from service.user_service import check_email_exists
class User:
    def __init__(self, name:str="", email:str=""):
        self.name = name
        self.email = email.strip()

    def validate_name(self):
        while True:
            name = input("what's your name: ")
            if len(name) < 2:
                raise ValueError("Invalid name")
            elif not name.replace(" ","").isalpha():
                continue
            self.name = name
            break

    def validate_email(self):
        while True:
            email = input("what is your email: ").strip()
            
            if not email.endswith("@gmail.com"):
                print("Email inválido: O domínio deve ser @gmail.com.")
                continue
            
            if check_email_exists(email): 
                print("Erro: Este e-mail já está cadastrado. Tente outro.")
                continue
            
            print("Sucesso! E-mail válido e disponível.")
            self.email = email
            break 

        