def main(dicionario, dados):
    print("\n-----------------------------------------------")
    print("Escolha a opção:")
    print("""    1 – Introduzir um Novo Cliente
    2 – Associar um Contacto de um Cliente
    3 – Associar um DNA a um Cliente
    4 – Testar Gene de um DNA
    5 – Excluir um Contacto de um Cliente
    6 – Consultar Agenda
    7 – Gravar Dados para ficheiro
    8 - Ler Dados de um ficheiro""")
    print("-----------------------------------------------")
    opcao = input("->")

    cliente = Pessoa()

    if opcao == '1':
        dicionario = cliente.novo_cliente(dicionario, dados)
        print(dicionario)
        main(dicionario, dados)
    elif opcao == '2':
        dicionario = cliente.novo_contato_cliente(dicionario)
        main(dicionario, dados)
    elif opcao == '3':
        dicionario = cliente.associar_DNA(dicionario)
        main(dicionario, dados)
    elif opcao == '4':
        print("main(dicioanrio, dados)")
    elif opcao == '5':
        dicionario = cliente.apagar_contato(dicionario)
        main(dicionario, dados)
    elif opcao == '6':
        cliente.agenda(dicionario)




    else:
        main(dicionario, dados)

if __name__ == '__main__':
    dicionario = {}
    dados = {}
    main(dicionario, dados)
