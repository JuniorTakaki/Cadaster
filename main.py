from cadastro import Cadastro
from produto import criar_tabela

def main():
    criar_tabela()  # garante que a tabela exista

    produto = Cadastro()
    produto.nome_produto()
    produto.quantidade_produto()
    produto.ano_produto()

    produto.salvar_no_banco()  # salva no banco

if __name__ == "__main__":
    main()

produto = Cadastro()
produto.nome_produto()
produto.quantidade_produto()
produto.ano_produto()