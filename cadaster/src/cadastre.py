class Cadastre:
    def __init__(self, name="", surname="", age=""):
        self.name = name
        self.surname = surname
        self.age = age

    def user_name(self):
        while True:
            name_input = input("Primeiro nome = ").strip()
            if not name_input:
                print("O campo não pode ficar vázio.")
            elif not name_input.isalpha():
                print("Use apenas letras, sem números ou símbolos")
                continue
            self.name = name_input
            break
        
    def user_surname(self):
        while True:
            surname_input = input("Sobrenome = ").strip()
            if not surname_input:
                print("O valor precisa ser preenchido")
            elif not surname_input.replace(" ", "").isalpha():
                print("Use apenas letras, sem números ou símbolos")
                continue
            self.surname = surname_input
            break
        
    def user_age(self):
        while True:
            age_input = input("Idade = ").strip()
            if not age_input:
                print("O valor precisa ser preenchido")
                continue
            try:
                self.age = int(age_input)
                if self.age < 18:
                    print("O usuário não tem idade insuficiente")
                else:
                    print(f"confirmado o ano {self.age} ")
                break
            except ValueError:
                print("Digite sua idade.")
    