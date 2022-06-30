######TORNEIO DE POKER########
import Jogadores

class jogo():
    def __init__(self):
        self.rodada = 0
        self.game = Jogadores.IA()
        print(self.game.maos)
    def players():
        jogadores = input('Número de desafiantes: ')
        jogadores=int(jogadores)+1
        return jogadores

    def ordem():
        lista = Jogadores.IA.get_players()
        print(lista)

    def partida():
        
        for rodada in range(5):
            if rodada == 0:
                maos = Jogadores.IA.get_maos()
                mesa = Jogadores.IA.get_mesa()

            

            ##########################
#            print(f'Rodada: {rodada}')
 #           print(f'Mão: |{maos[0][2]}| |{maos[0][3]}|')
  #          print(f'Saldo: {maos[0][1]} coins')
