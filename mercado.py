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
                continuar= input('continuar: S/N ')

                print('produto adicionado')
                #print(produtos)   #teste
                
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
                continuar= input('continuar: S/N ')

                print(nome,' deletado')
                #print(produtos)   #teste
                                
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
            def todos():
                #nome=(hora de entrada, saída, id)
                ana=(8,12,1,'ana')
                joao=(9,15,2,'joao')
                jose=(11,18,3,'jose')
                alberto=(15,17,4,'alberto')
                luis=(16,20,5,'luis')
                tadeu=(17,20,6,'tadeu')
                lista=[ana,joao,jose,alberto,luis,tadeu]
                return lista
                
            def horario(horario,lista):
                abertos=0
                
                for c in range(len(lista)):
                    if lista[c][0]<=horario<lista[c][1]:
                        abertos+=1
                return abertos

            def exibir():
                print(
                '\n id=1 ana'
                '\n id=2 joao'
                '\n id=3 jose'
                '\n id=4 alberto'
                '\n id=5 luis'
                '\n id=6 tadeu'
                '\n'
                '\n'
                '\n'
                )
                return
            def salario(lista):
                funcionario = int(input("Digite o ID: "))
                for i in range(len(lista)):
                    if lista[i][2]==funcionario:
                        entrada= lista[i][0]
                        saida= lista[i][1]
                        recebe = (saida-entrada)*28*20     #horas trabalhadas//dias no mês//salario por hora
                        print()
                        print(lista[i][3], 'tem o salário de R$', recebe)
                        print()

                return
            
        class clientes():
            def totais():
                return
            def media_de_compra():
                return
            def dados():
                return

from datetime import datetime
produtos= mercado.produtos.todos()
lista= mercado.pessoas.funcionarios.todos()
while True:

    hora= int(datetime.today().strftime('%H'))
    horario= mercado.pessoas.funcionarios.horario(hora,lista)

    print(datetime.today().strftime('%d-%m %H:%M'))
    print("------------------------------------------------------")
    print('(1)Ver produtos disponíveis')
    print('(2)Adicionar produtos novos')
    print('(3)Remover produtos')
    print('(4)Ver funcionarios')
    print('(5)salario do funcionario')
    print('(0)Sair')
    print("Neste horário há", horario ,"caixas abertos")
    
    opcao = input()
    
    if opcao=="0":
        break
    elif opcao == "1":
        mercado.produtos.ver_produtos(produtos)
    elif opcao=="2":
        mercado.produtos.inserir(produtos)
    elif opcao=="3":
        mercado.produtos.deletar()
    elif opcao=="4":
        mercado.pessoas.funcionarios.exibir()
    elif opcao=="5":
        mercado.pessoas.funcionarios.exibir()       #!IMPORTANTE
        mercado.pessoas.funcionarios.salario(lista)
    else:
        print("///////////////////opção inválida///////////////////")
