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
            if 'N' in continuar.upper():
                    break


    def abertos(horario):
        abertos=0
        ana=(8,12)
        if ana[0]<horario<ana[1]:
            abertos+=1
        joao=(9,15)
        if joao[0]<horario<joao[1]:
            abertos+=1
        jose=(11,18)
        if jose[0]<horario<jose[1]:
            abertos+=1
        alberto=(15,17)
        if alberto[0]<horario<alberto[1]:
            abertos+=1
        luis=(16,20)
        if luis[0]<horario<luis[1]:
            abertos+=1
        tadeu=(17,20)
        if tadeu[0]<horario<tadeu[1]:
            abertos+=1
        return abertos
    
    
horario=14  #importar lib horario atual
#print("Neste horário há", abertos(horario) ,"caixas abertos")



#mercado.deletar() 
#mercado.inserir()

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


    
     
    