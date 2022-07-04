import random

class baralho:
    def __init__(self,jogam):        
        self.players = jogam  
        cartasNumero = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        cartasNaipe = ['♠️','♥️','♦️', '♣️']
        cartasSeparadas = []
        self.tot_cartas = 0 

        for a in range(len(cartasNumero)):                         
            for b in range(len(cartasNaipe)):
                cartasSeparadas.append(f'{cartasNumero[a]}{cartasNaipe[b]}')
                self.tot_cartas +=1
        random.shuffle(cartasSeparadas)
        self.cartasEmbaralhadas = cartasSeparadas

    def distribuir(self, lista):                      
        cartas = self.cartasEmbaralhadas                                          
        decks = lista
        mesa=[]

        cartasTotal = self.tot_cartas 

        for c in range(1):
            for j in range(self.players):                                
                cartaMovida = cartas[0]
                lista[j].append(cartaMovida)
                cartas.remove(cartaMovida)
                cartasTotal -=1

        for t in range(5):
            mesa.append(cartas[t])
        return [decks, mesa]

    def nova_partida(lista):
        mesa = []
        get = baralho(len(lista))
        cartas = get.cartasEmbaralhadas  


        for j in range(len(lista)):                                
            cartaMovida = cartas[0]
            lista[j][2]=cartaMovida
            cartas.remove(cartaMovida)
        for j in range(len(lista)):                                
            cartaMovida = cartas[0]
            lista[j][3]=cartaMovida
            cartas.remove(cartaMovida)

        for t in range(5):
            mesa.append(cartas[t])
        return [lista, mesa]
        







