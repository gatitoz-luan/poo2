import poker
import deck
import mao
import random

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

    def bot(mesa,lista):
        aposta_antes = lista[4]
        cartas = lista[2:4]
        sorte = int(mao.verifica.testes(mesa[1],cartas))
        
        if sorte>100:
            aposta = lista[1]
        if sorte>50:
            aposta = mesa[0][1]
        if sorte<=50:
            x = random.randint(0,10)
            if x>2:
                if x>7:
                    aposta = mesa[0][1]
                else:
                    aposta = mesa[0][0]
            else:
                aposta = 0
                lista[5] = 0

        if aposta > lista[1]:
            aposta = lista[1]
        lista[4] = aposta+ aposta_antes
        lista[1] -= aposta
        if aposta>0:
            if lista[1]==0:
                print(f'{lista[0]} apostou ALL IN')
            elif aposta == mesa[0][0]:
                print(f'{lista[0]} pagou a aposta')
            else:
                print(f'{lista[0]} apostou {aposta:.0f}')

            if aposta == aposta_antes:
                mesa[0][0]=aposta*2
            else:
                mesa[0][0]=aposta
            mesa[0][1]+=aposta
            
        else:
            print(f'{lista[0]} desistiu')
        return [mesa[0], lista]








game = IA()
IA.cria_players(game)
lista = IA.dar_fichas(game)
jogam = game.jogam
decks = deck.baralho(jogam)
maos = deck.baralho.distribuir(decks, lista)[0]
mesa = deck.baralho.distribuir(decks, lista)[1]
poker.jogo.partida()

