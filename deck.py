import random                                                                   #biblioteca que gera aleatórios

class baralho:                                                                  #Classe principal
            
    jogadores = 9                                                               #Define o número de jogadores e quais números e naipes estarão em jogo
    cartasNumero = ['A','2','3','4','5','6','7','8','9','J','Q','K']
    cartasNaipe = ['paus','ouros','espadas', 'copas']
    cartasSeparadas = []                                                        #lista que armazená todas cartas do baralho

    for a in range(len(cartasNumero)):                                          #laço que "cria" cartas, combinando numero e naipe
        for b in range(len(cartasNaipe)):
            cartasSeparadas.append(f'{cartasNumero[a]} de {cartasNaipe[b]}')

    cartasTotal = len(cartasSeparadas)                                          #armazena quantidade de cartas

 
    def embaralhar():                                                           #função que coloca a lista de cartas em ordem aleatória
        cartas = baralho.cartasSeparadas                                        
        cartasEmbaralhadas = []                                                 #lista que receberá o baralho embaralhado

        for c in range(baralho.cartasTotal):                                    #laço para cada carta
            cartaMovida = cartas[random.randrange(0,len(cartas))]               #seleciona uma carta
            cartasEmbaralhadas.append(cartaMovida)                              #a carta selecionada vai para o topo do baralho
            cartas.remove(cartaMovida)                                          

        return cartasEmbaralhadas
    
    def distribuir(embaralhadas):                                               #função que cria o deck de cada jogador
        cartas = embaralhadas                                           
        decks = []                                                              #listas que armazenam os decks individuais, cartas extras e junção de todos os deck
        deckIndividual = []
        deckInicial = []
        jogam = baralho.jogadores       
        cartasTotal = baralho.cartasTotal                                       #variaveis de numeração de cartas e jogadores
        jogadoresComCartas = 0                              
        

        while True:                                                             #laço para distribuição de cartas
            
            for j in range(cartasTotal//jogam):                                 #laço que distribuir uma quantidade igual de cartas aleatórias para cada jogador
                cartaMovida = cartas[random.randrange(0,len(cartas))]
                deckIndividual.append(cartaMovida)
                cartas.remove(cartaMovida)
                #print(cartaMovida)

            deckInicial = deckIndividual.copy()                                 #definindo o deck considerando que todos tem o mesmo número de cartas
            decks.append(deckInicial)
            deckIndividual.clear()
            jogadoresComCartas +=1
            #print(deckInicial)

            if len(cartas)==(cartasTotal%jogam):                                #condição de quando se tratar de cartas extras
                for x in range(len(cartas), -1 , -1):
                    cartaMovida = cartas[random.randrange(0,len(cartas))]
                    decks[x].append(cartaMovida)                                #alguns jogadores começam com 1 carta a mais
                break
        #print(decks)
        return decks



embaralhadas = baralho.embaralhar()                                             #chama função que cria e embaralha as cartas
distribui = baralho.distribuir(embaralhadas)                                    #chama função distribui as cartas
for z in range (baralho.jogadores):
    print(f"O deck do jogador {z+1} contem as cartas: {', '.join(distribui[z])}.")           #exibe lista com deck de cada jogador






