######TORNEIO DE POKER########
import Jogadores
import deck
import time
import mao
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
            

            for rodada in range(4):
                
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

                if rodada == 1:
                    mesa_on[1].extend(mesa[0:3])
                if rodada == 2:
                    mesa_on[1].append(mesa[3])
                if rodada == 3:
                    mesa_on[1].append(mesa[4])
                    
                for i in range(joga,len(lista)):
                    if len(mesa_on[1])>0:
                        print(mesa_on[1])
                    print(f'Aposta: {mesa_on[0][0]}')
                    print(f'Prêmio: {mesa_on[0][1]}')
                    time.sleep(1)
                    if lista[i][0] != 'Player' and lista[i][5]==1:
                        jogou = Jogadores.IA.bot(mesa_on,lista[i])
                        lista[i] = jogou[1]
                        mesa_on[0] = jogou[0]
                    elif lista[i][0] == 'Player'and lista[i][5]==1:
                        print(f'Mão: |{maos[0][2]}| |{maos[0][3]}|')
                        print(f'Saldo: {maos[0][1]} coins')
                        print('[1] Desistir     [2] Pagar   [3] Apostar')
                        opcao = input('digite: ')
                        aposta = 0
                        if opcao == '1':
                            print('Desisto')
                            aposta = 0
                            lista[0][5] = 0
                        if opcao == '2':
                            print('Paguei')
                            aposta = mesa_on[0][0]
                        if opcao == '3':
                            while True:
                                aposta = int(input('valor: '))
                                if aposta > mesa_on[0][0] and aposta < lista[0][1]:
                                    break
                                else:
                                    print('!!!VALOR INVALIDO, TENTE NOVAMENTE!!!')
                        lista[0][4] += aposta
                        lista[0][1] -= aposta
                        mesa_on[0][0]=aposta
                        mesa_on[0][1]+=aposta
                    if i == big_blind[0]:
                        break

                for i in range(joga):
                    time.sleep(1)
                    if len(mesa_on[1])>0:
                        print(mesa_on[1])
                    print(f'Aposta: {mesa_on[0][0]}')
                    print(f'Prêmio: {mesa_on[0][1]}')
                    if lista[i][0] != 'Player' and lista[i][5]==1:
                        Jogadores.IA.bot(mesa_on,lista[i])
                        lista[i] = jogou[1]
                        mesa_on[0] = jogou[0]
                    elif lista[i][0] == 'Player'and lista[i][5]==1:
                        print(f'Mão: |{maos[0][2]}| |{maos[0][3]}|')
                        print(f'Saldo: {maos[0][1]} coins')
                        print('[1] Desistir     [2] Pagar   [3] Apostar')
                        opcao = input('digite: ')
                        aposta = 0
                        if opcao == '1':
                            print('Desisto')
                            aposta = 0
                            lista[0][5] = 0
                        if opcao == '2':
                            print('Paguei')
                            aposta = mesa_on[0][0]
                        if opcao == '3':
                            while True:
                                aposta = int(input('valor: '))
                                if aposta > mesa_on[0][0] and aposta < lista[0][1]:
                                    break
                                else:
                                    print('!!!VALOR INVALIDO, TENTE NOVAMENTE!!!')
                        lista[0][4] += aposta
                        lista[0][1] -= aposta
                        mesa_on[0][0]=aposta
                        mesa_on[0][1]+=aposta
                    if i == big_blind[0]:
                        break
            
            compara_pontos = []
            for c in range(len(lista)):
                pontos = mao.verifica.testes(mesa,lista[c][2:4])
                if lista[c][5]==1:
                    compara_pontos.append(pontos)
                else:
                    compara_pontos.append(0)

            max_value = max(compara_pontos)
            id_vence = []
            for idx in range(len(compara_pontos)):
                if (compara_pontos[idx] == max_value):
                    id_vence.append(idx)
            divide = len(id_vence)
            for k in range(divide):
                lista[id_vence[k]][1] += mesa_on[0][1]
                print(f'{lista[0]} recebeu {mesa_on[0][1]}')

            dealer+=1
            small= small*2
            for i in range(len(lista)):
                lista[i][4]= 0
            deck.baralho.nova_partida(lista)

            ##########################
#            print(f'Rodada: {rodada}')
 #           print(f'Mão: |{maos[0][2]}| |{maos[0][3]}|')
  #          print(f'Saldo: {maos[0][1]} coins')
