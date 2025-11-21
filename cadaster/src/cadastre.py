class Cadastre:
    def __init__(self, name =" ", surname=" ", year= " "):
        self.name = name
        self.surname = surname
        self.year = year

    def user_name(self):
        while True:
            name_input = str(input("Primeiro nome = ")).strip()
            if not name_input:
                print("O campo não pode ficar vázio.")
            elif not name_input.isalpha():
                print("Use apenas letras, sem números ou símbolos")
                continue
            self.name = name_input
            break
        
    def user_surname(self):
        while True:
            surname_input = str((input("Sobrenome = "))).strip()
            if not surname_input:
                print("O valor precisa ser preenchido")
            elif not surname_input.replace(" ", "").isalpha():
                print("Use apenas letras, sem números ou símbolos")
                continue
            self.surname = surname_input
            break
        
    def user_year(self):
        while True:
            year_input = input("Idade = ").strip()
            if not year_input:
                print("O valor precisa ser preenchido")
                continue
            try:
                self.year = int(year_input)
                if self.year < 18:
                    print("O usuário não tem idade insuficiente")
                else:
                    print(f"confirmado o ano {self.year} ")
                break
            except ValueError:
                print("Digite sua idade.")
    