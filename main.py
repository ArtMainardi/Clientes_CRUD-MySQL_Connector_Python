from produtos import *
from relatorio import *

while True:
    print("\n===== SISTEMA DE PRODUTOS =====")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Buscar produto")
    print("4 - Atualizar preço")
    print("5 - Excluir produto")
    print("6 - Quantidade de cada produto")
    print("7 - Valor total do estoque")
    print("8 - Produto mais caro")
    print("0 - Sair")

    opcao = input("Opção: ")

    if opcao == "1":
        nome = input("Nome: ")
        preco = float(input("Preço: "))
        qtd = int(input("Quantidade: "))
        cat = input("Categoria: ")
        cadastrar_produto(nome, preco, qtd, cat)
    elif opcao == "2":
        listar_produtos()
    elif opcao == "3":
        termo = input("Buscar por nome: ")
        buscar_produto(termo)
    elif opcao == "4":
        pid = int(input("ID do produto: "))
        novo = float(input("Novo preço: "))
        atualizar_preco(pid, novo)
    elif opcao == "5":
        pid = int(input("ID do produto: "))
        excluir_produto(pid)
    elif opcao == "6":
        total_produtos()
    elif opcao == "7":
        valor_total_estoque()
    elif opcao == "8":
        produto_mais_caro()
    elif opcao == "0":
        print("Encerrando...")
        break
    else:
        print("Opção inválida!")