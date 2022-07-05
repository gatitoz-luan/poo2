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
        while True:
            jogadores = input('Número de desafiantes: ')
            if int(jogadores) > 1 and int(jogadores)<8:
                break
            print('!!!VALOR INVALIDO, TENTE NOVAMENTE!!!')
            
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
                lista[i].append(1)  #para ativos na torneio
        for c in range(3):
            if c == 2:
                print('--------Preparando Torneio--------')
            print('.')
            time.sleep(1)
        
        while True:
            quebra = 0
            deletar = []
            for j in range (len(lista)):
                if lista[j][1] > 0:
                    lista[j][5] = 1
                else:
                    deletar.append(j)
            for r in range(len(deletar)):
                deletado =deletar[r]-r
                print(f'{lista[deletado][0]} Foi Eliminado')
                del lista[deletado]
            if len(lista)==1:
                print(f'!!!!!!!!!!!!!!!!!!!!! {lista[0][0]} é o vencedor do Torneio !!!!!!!!!!!!!!!!!!!!!')
                break
            big_blind = [(dealer+2)%len(lista), small*2]
            small_blind = [(dealer+1)%len(lista), small]
            small *= 2
            piso=big_blind[1]
            premio= small_blind[1]+piso
            joga= (dealer+3)%len(lista)
            for c in range(5):
                if c == 2:
                    print('++++++++Preparando Partida++++++++')
                print('.')
                time.sleep(1)
            for d in range(len(lista)):
                print(f'saldo do {lista[d][0]} é {lista[d][1]}')
                time.sleep(0.5)



            for rodada in range(4):
                for c in range(len(lista)):
                    lista[c][4]=0
                if rodada == 0:
                    maos = Jogadores.IA.get_maos()
                    mesa = Jogadores.IA.get_mesa()
                    
                    mesa_on = [[piso,premio],[]]
                    lista[small_blind[0]][4]=small_blind[1]
                    lista[small_blind[0]][1]-= small_blind[1]
                    lista[big_blind[0]][4]=big_blind[1]
                    lista[big_blind[0]][1]-= big_blind[1]

                    print(f'{lista[dealer%len(lista)][0]} é o Dealer')
                    time.sleep(1)
                    print(f'{lista[small_blind[0]][0]} pagou {small_blind[1]}')
                    time.sleep(1)
                    print(f'{lista[big_blind[0]][0]} pagou {big_blind[1]}')

                if rodada == 1:
                    mesa_on[1].extend(mesa[0:3])
                if rodada == 2:
                    mesa_on[1].append(mesa[3])
                if rodada == 3:
                    mesa_on[1].append(mesa[4])


                for t in range(0,5):
                    for i in range(0,len(lista)):
                        if t==0 and i<joga:
                            continue
                        if lista[i][5] == 0:
                            continue
                        if lista[i][1] == 0:
                            continue
                        
                        if mesa_on[0][0]== lista[i][4]:
                            quebra =1
                            break
                        if lista[i][1]>0:
                            if len(mesa_on[1])>0:
                                print(mesa_on[1])
                            print('.')
                            time.sleep(1)
                            print(f'Aposta: {mesa_on[0][0]:.0f}')
                            print(f'Prêmio: {mesa_on[0][1]:.0f}')
                            time.sleep(1)
                            if lista[i][0] != 'Player':
                                jogou = Jogadores.IA.bot(mesa_on,lista[i])
                                lista[i] = jogou[1]
                                if jogou[0][0] > 0:
                                    mesa_on[0] = jogou[0]
                            elif lista[i][0] == 'Player':
                                print(f'Mão: |{maos[0][2]}| |{maos[0][3]}|')
                                print(f'Saldo: {maos[0][1]:.0f} coins')
                                print('[1] Desistir     [2] Pagar   [3] Apostar')
                                
                                while True:
                                    opcao = input('digite: ')
                                    if opcao == '1':
                                        print('Desisto')
                                        aposta = 0
                                        lista[i][5] = 0
                                        break
                                    elif opcao == '2':
                                        print('Paguei')
                                        aposta = mesa_on[0][0]
                                        break
                                    elif opcao == '3':
                                        while True:
                                            aposta = int(input('valor: '))
                                            if aposta > mesa_on[0][0] and aposta <= lista[0][1]:
                                                print(f'Apostei {aposta}')
                                                break
                                            else:
                                                print('!!!VALOR INVALIDO, TENTE NOVAMENTE!!!')
                                        break
                                    print('!!!VALOR INVALIDO, TENTE NOVAMENTE!!!')
                                if aposta > lista[i][1]:
                                    aposta = lista[1]
                                lista[0][4] += aposta
                                lista[0][1] -= aposta
                                if aposta > 0:
                                    mesa_on[0][0]=aposta
                                else:
                                    mesa_on[0][0]=mesa_on[0][0]
                                mesa_on[0][1]+=aposta






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
                lista[id_vence[k]][1] += mesa_on[0][1]//divide
                print(f'{lista[id_vence[k]][0]} recebeu {mesa_on[0][1]//divide:.0f}')
                vence = []
                vence.extend(lista[id_vence[k]][2:4])
                vence.extend(mesa_on[1])
                print(f'Cartas: {vence}')

            dealer+=1
            small= small*2
            for i in range(len(lista)):
                lista[i][4]= 0
            deck.baralho.nova_partida(lista)

