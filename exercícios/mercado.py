# Mercado é um local onde as pessoas compram diversos produtos, os produtos possuem preços e quantidades,
# novos produtos podem ser adicionados, como também podem ser removidos.

class mercado():
    class produtos():
        def todos():
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
                elif continuar.upper() != 'S':
                    while True:
                        continuar= input('**OPÇÃO INVALIDA** continuar: S/N ')
                        if continuar.upper() == 'S' or continuar.upper() == 'N':
                           break
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
                elif continuar.upper() != 'S':
                    while True:
                        continuar= input('**OPÇÃO INVALIDA** continuar: S/N ')
                        if continuar.upper() == 'S' or continuar.upper() == 'N':
                           break
                if 'N' in continuar.upper():
                    break
                    
    class pessoas():
        class funcionarios():
            def horario(horario):
                abertos=0
                ana=(8,12)
                joao=(9,15)
                jose=(11,18)
                alberto=(15,17)
                luis=(16,20)
                tadeu=(17,20)
                
                if ana[0]<=horario<ana[1]:
                    abertos+=1
                
                if joao[0]<=horario<joao[1]:
                    abertos+=1
                
                if jose[0]<=horario<jose[1]:
                    abertos+=1
                    
                if alberto[0]<=horario<alberto[1]:
                    abertos+=1
                    
                if luis[0]<=horario<luis[1]:
                    abertos+=1
                
                if tadeu[0]<=horario<tadeu[1]:
                    abertos+=1
                return abertos
            def info():
            
        class clientes():
            def totais():
            def media_de_compra():
            def dados():

from datetime import datetime



produtos= mercado.produtos.todos()

while True:
    print(datetime.today().strftime('%d-%m %H:%M'))
    print("------------------------------------------------------")
    print('(1)Ver produtos disponíveis')
    print('(2)Adicionar produtos novos')
    print('(3)Remover produtos')
    print('(0)Sair')
    
    hora= datetime.today().strftime('%H')
    horario= mercado.pessoas.funcionarios.horario(hora)
    print("Neste horário há", abertos(horario) ,"caixas abertos")
    opcao = input()
    
    if opcao=="0":
        break
    elif opcao == "1":
        mercado.produtos.ver_produtos(produtos)
    elif opcao=="2":
        mercado.produtos.inserir(produtos)
    elif opcao=="3":
        mercado.produtos.deletar()
    else:
        print("///////////////////opção inválida///////////////////")
