import clientes


def exibir_menu():
    print("\n" + "=" * 35)
    print("    SISTEMA DE GESTÃO DE CLIENTES")
    print("=" * 35)
    print("1 - Cadastrar novo cliente")
    print("2 - Listar todos os clientes")
    print("3 - Buscar cliente por ID")
    print("4 - Atualizar cliente")
    print("5 - Deletar cliente")
    print("0 - Sair")
    print("=" * 35)


def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            print("\n--- CADASTRAR CLIENTE ---")
            nome = input("Nome: ").strip()
            email = input("E-mail (deixe em branco se não houver): ").strip()
            telefone = input("Telefone (deixe em branco se não houver): ").strip()

            if nome:
                novo_cliente = clientes.cliente(nome, email, telefone)
                clientes.criar(novo_cliente)
            else:
                print("O nome do cliente é obrigatório!")

        elif opcao == "2":
            print("\n--- LISTA DE CLIENTES ---")
            clientes.listar()

        elif opcao == "3":
            print("\n--- BUSCAR CLIENTE ---")
            id_busca = input("Digite o ID do cliente: ").strip()
            if id_busca.isdigit():
                clientes.buscar(int(id_busca))
            else:
                print("Por favor, digite um ID numérico válido.")

        elif opcao == "4":
            print("\n--- ATUALIZAR CLIENTE ---")
            id_atualizar = input("Digite o ID do cliente a ser atualizado: ").strip()

            if id_atualizar.isdigit():
                nome = input("Novo Nome: ").strip()
                email = input("Novo E-mail (deixe em branco se não houver): ").strip()
                telefone = input("Novo Telefone (deixe em branco se não houver): ").strip()

                if nome:
                    # Instancia o cliente e atribui o ID necessário para a consulta SQL do UPDATE
                    cliente_editado = clientes.cliente(nome, email, telefone)
                    cliente_editado.id = int(id_atualizar)
                    clientes.atualizar(cliente_editado)
                else:
                    print("O nome é obrigatório.")
            else:
                print("Por favor, digite um ID numérico válido.")

        elif opcao == "5":
            print("\n--- DELETAR CLIENTE ---")
            id_deletar = input("Digite o ID do cliente que deseja remover: ").strip()
            if id_deletar.isdigit():
                confirmacao = input(f"Tem certeza que deseja deletar o ID {id_deletar}? (S/N): ").strip().upper()
                if confirmacao == "S":
                    clientes.deletar(int(id_deletar))
            else:
                print("Por favor, digite um ID numérico válido.")

        elif opcao == "0":
            print("\nEncerrando o programa... Até logo!")
            break

        else:
            print("\nOpção inválida! Tente novamente.")


if __name__ == "__main__":
    main()