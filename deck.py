import random

class baralho:
    
    jogadores = 9
    cartasNumero = ['A','2','3','4','5','6','7','8','9','J','Q','K']
    cartasNaipe = ['paus','ouro','espadas', 'copa']
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
        jogam = baralho.jogadores
        
        for i in range(jogam):
            decks.append(deckIndividual)
    
        for j in range(baralho.cartasTotal):
            for g in range(len(jogam)):
        pass



embaralhadas = baralho.embaralhar()  
distribui = baralho.distribuir(embaralhadas)