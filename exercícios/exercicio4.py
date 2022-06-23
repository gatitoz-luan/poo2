import propriedade

while True:
    try:
        preco = int(input('Base de preço da propriedade: '))
        escolha = int(input('[1] Propriedade Nova\n[2] Propriedade Velha\n'))

        if escolha==1:
            endereco= input('Endereço: ')
            precoAdicional = int(input('Preço Adicional: '))
            lar = propriedade.novo(endereco, preco, precoAdicional)

        elif escolha==2:
            endereco= input('Endereço: ')
            lar = propriedade.velho(endereco, preco)
        
        print(lar.getPreco())
    
    except EOFError:
        break