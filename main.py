from cadastro import Cadastro
from produto import criar_tabela, salvar_no_banco

def main():
    criar_tabela()

    nome = input("Nome do produto: ")
    quantidade = int(input("Quantidade: "))
    ano = int(input("Ano: "))

    salvar_no_banco(nome, quantidade, ano)


if __name__ == "__main__":
    main()
