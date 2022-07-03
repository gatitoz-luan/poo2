######TORNEIO DE POKER########
import Jogadores

class jogo():
    def __init__(self):
        self.rodada = 0
        self.game = Jogadores.IA()
    def players():
        jogadores = input('Número de desafiantes: ')
        jogadores=int(jogadores)+1
        return jogadores

    def ordem(lista):
        pass

    def partida():
        dealer = 0
        small= 5
        lista = Jogadores.IA.get_players()
        for i in range(len(lista)):
                lista[i].append(0)  #apostas
                lista[i].append(1)  #para ativos no torneio
        while True:
            for j in range (len(lista)):
                if lista[j][1] > 0:
                    lista[j][5] = 1
                else:
                    del lista[j]
            big_blind = [dealer+2%len(lista), small*2]
            small_blind = [dealer+1%len(lista), small]
            small *= 2
            piso=big_blind[1]
            premio= small_blind[1]+piso
            joga= dealer+3%len(lista)
            

            for rodada in range(5):
                
                if rodada == 0:
                    maos = Jogadores.IA.get_maos()
                    mesa = Jogadores.IA.get_mesa()
                    mesa_on = [[piso,premio],[]]
                    lista[small_blind[0]][4]=small_blind[1]
                    lista[small_blind[0]][1]-= small_blind[1]
                    lista[big_blind[0]][4]=big_blind[1]
                    lista[big_blind[0]][1]-= big_blind[1]

                    print(f'Mão: |{maos[0][2]}| |{maos[0][3]}|')
                    print(f'Saldo: {maos[0][1]} coins')
                    
                    print(f'{lista[dealer][0]} é o Dealer')
                    print(f'{lista[small_blind[0]][0]} pagou {small_blind[1]}')
                    print(f'{lista[big_blind[0]][0]} pagou {big_blind[1]}')

                    
                for i in range(joga,len(lista)):
                    if lista[i][0] != 'Player' and lista[i][5]==1:
                        jogou = Jogadores.IA.bot(mesa_on,lista[i])
                        print(jogou)
                        lista[i] = jogou[1]
                        mesa_on = jogou[0]
                    else:
                        print('joguei')
                    if i == big_blind[0]:
                        break

                for i in range(len(lista)):
                    if lista[i][0] != 'Player' and lista[i][5]==1:
                        Jogadores.IA.bot(mesa_on,lista[i])
                        lista[i] = jogou[1]
                        mesa_on = jogou[0]
                    else:
                        print('joguei')
                    if i == big_blind[0]:
                        break


            dealer+=1
            small= small*2
            for i in range(len(lista)):
                lista[i][4]= 0

            ##########################
#            print(f'Rodada: {rodada}')
 #           print(f'Mão: |{maos[0][2]}| |{maos[0][3]}|')
  #          print(f'Saldo: {maos[0][1]} coins')
