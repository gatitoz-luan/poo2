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
        aposta = 0
        cartas = lista[2:4]
        recebe = mao.verifica.testes(mesa[1],cartas)
        sorte = int(recebe[0])
        confiança = random.randint(1,21)
        if confiança==1:
            aposta = 0
            lista[5] = 0
        elif confiança == 20:
            aposta = lista[1]
        else:
            if sorte>100:
                if confiança> 10:
                    aposta = lista[1]
                elif confiança>5:
                    aposta =mesa[0][1]
                else:
                    aposta = mesa[0][0]
            elif sorte>50:
                if confiança> 15:
                    aposta = lista[1]
                elif confiança> 10:
                    aposta = mesa[0][1]
                elif confiança>5:
                    aposta =mesa[0][0]
                else:
                    aposta = 0
            else:
                if confiança> 15:
                    aposta = mesa[0][1]
                else:
                    if mesa[0][0] < (lista[1]/2):
                        if confiança> 10:
                            aposta = mesa[0][0]
                        elif confiança>5:
                            aposta = 0
                    else:
                        aposta = 0

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
            lista[5]=0
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

