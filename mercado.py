class mercado():
    def produtos():
        produtos = {"banana":2, "queijo":3, "pão":1}
        return produtos

    def ver_produtos(produtos):
        print(produtos)
        
    def inserir(produtos):
        while True:
            nome = input('produto: ')
            quantidade = input('quantidade: ')
            produtos[nome]= quantidade
            print('produto adicionado')
            print(produtos)   #teste
            continuar= input('continuar: S/N ')
            if 'N' in continuar.upper():
                break
    def deletar():
        while True:
            nome = input('produto: ')
            if nome in produtos.keys():
                del produtos[nome]
            print(nome,' deletado')
            print(produtos)   #teste
            continuar= input('continuar: S/N ')
            if 'N' in continuar.upper():
                    break

while True:
    produtos= mercado.produtos()
    print("------------------------------------------------------")
    print('(1)Ver produtos disponíveis')
    print('(2)Adicionar produtos novos')
    print('(3)Remover produtos')
    print('(0)Sair')
    opcao = input()
    
    if opcao=="0":
        break
    elif opcao == "1":
        mercado.ver_produtos(produtos)
    elif opcao=="2":
        mercado.inserir(produtos)
    elif opcao=="3":
        mercado.deletar()
    else:
        print("///////////////////opção inválida///////////////////")
