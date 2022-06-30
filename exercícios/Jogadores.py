import poker
import deck

class IA():
    def __init__(self):
        self.players = []
        self.jogam = poker.jogo.players()

    def cria_players(self):
        for i in range(self.jogam):
            if i==0:
                self.players.append(['Player'])
            else:
                self.players.append(['Desafiante'+str(i)])
        return self.players
        
    def dar_fichas(self):
        for j in range(len(self.players)):
            self.players[j].append(1000)
        return self.players
    
    def get_maos():
        return maos
    def get_mesa():
        return mesa
    def get_players():
        return lista

    




game = IA()
IA.cria_players(game)
lista = IA.dar_fichas(game)
jogam = game.jogam
decks = deck.baralho(jogam)
maos = deck.baralho.distribuir(decks, lista)[0]
mesa = deck.baralho.distribuir(decks, lista)[1]
poker.jogo.partida()
poker.jogo.ordem()

