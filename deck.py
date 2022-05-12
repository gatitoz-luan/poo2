import random

class baralho:
    
    jogadores = 9
    cartasNumero = ['A','2','3','4','5','6','7','8','9','J','Q','K']
    cartasNaipe = ['paus','ouro','espadas', 'copas']
    cartasSeparadas = []

    for a in range(len(cartasNumero)):
        for b in range(len(cartasNaipe)):
            cartasSeparadas.append(f'{cartasNumero[a]} de {cartasNaipe[b]}')

    cartasTotal = len(cartasSeparadas)

    def __init__(self):
        pass

    def embaralhar():
        cartas = baralho.cartasSeparadas
        cartasEmbaralhadas = []

        for c in range(baralho.cartasTotal):
            cartaMovida = cartas[random.randrange(0,len(cartas))]
            cartasEmbaralhadas.append(cartaMovida)
            cartas.remove(cartaMovida)
            
        return cartasEmbaralhadas
    
    def distribuir(embaralhadas):
        cartas = embaralhadas
        decks = []
        deckIndividual = []
        deckInicial = []
        jogam = baralho.jogadores
        cartasTotal = baralho.cartasTotal
        jogadoresComCartas = 0
        

        while True:
            
            for j in range(cartasTotal//jogam):
                cartaMovida = cartas[random.randrange(0,len(cartas))]
                deckIndividual.append(cartaMovida)
                cartas.remove(cartaMovida)
                #print(cartaMovida)

            deckInicial = deckIndividual.copy()
            decks.append(deckInicial)
            deckIndividual.clear()
            jogadoresComCartas +=1
            #print(deckInicial)

            if len(cartas)==(cartasTotal%jogam):
                for x in range(len(cartas), 0 , -1):
                    cartaMovida = cartas[random.randrange(0,len(cartas))]
                    decks[x].append(cartaMovida)
                break
        print(decks)
        



embaralhadas = baralho.embaralhar()  
distribui = baralho.distribuir(embaralhadas)