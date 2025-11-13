
class Cadastro:
    def __init__(self, nome =" ", quantidade=" ", ano= " "):
        self.nome = nome
        self.quantidade = quantidade
        self.ano = ano

    def nome_produto(self):
        while True:
            self.nome = str(input("Produto = ")).strip() 
            if not self.nome:
                print("O campo não pode ficar vázio.")
                continue
            print(f"{self.nome} cadastrado com sucesso.")
            break
        
    def quantidade_produto(self):
        while True:
            entrada = input("Quantidade = ").strip()
            if not entrada:
                print("O valor precisa ser preenchido")
                continue
            try:
                self.quantidade = int(entrada) # conversão para int
                if self.quantidade == 0:       # validar como um valor int
                    print("Valor inserido é invalido")
                    continue
                print(f"Foi cadastrado {self.quantidade} quantidades no sistema.")
                break
            except ValueError:
                print("Digite apenas números válidos.")

    def ano_produto(self):
        while True:
            ano_lancamento = input('Ano de fabricação = ').strip()
            if not ano_lancamento:
                print("O valor precisa ser preenchido")
                continue
            try:
                self.ano = int(ano_lancamento)
                if self.ano < 2000:
                    print("O produto não pode ser cadastrado")
                else:
                    print(f"confirmado o ano {self.ano} ")
                break
            except ValueError:
                print("Digite apenas números válidos.")