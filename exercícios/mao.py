

class verifica:
    
    def testes(mesa,mao):
        pontos=0
        cartas = []
        cartas.extend(mesa)
        cartas.extend(mao)
        cartas.sort()

        while True:
            x = verifica.Royal_flush(cartas)
            if type(x) is list:
                pontos = 99999900
                return pontos

            y = verifica.Straight_flush(cartas)
            if type(y) is list:
                if y[0][0]=='A':
                    pontos = 1999900
                else:
                    pontos = int(y[0][0])*1000000
                return pontos

            z = verifica.Quadra(cartas)
            if type(z) is not bool:
                if z=='A':
                    pontos = 990000
                elif z=='K':
                    pontos = 980000
                elif z=='Q':
                    pontos = 970000
                elif z=='J':
                    pontos = 960000
                elif z=='1':
                    pontos = 950000
                else:
                    pontos = int(z)*100000
                return pontos

            j = verifica.Full_House(cartas)
            if type(j) is list:
                if j[0]=='A':
                    pontos = 99000
                elif j[0]=='K':
                    pontos = 98000
                elif j[0]=='Q':
                    pontos = 97000
                elif j[0]=='J':
                    pontos = 96000
                elif j[0]=='1':
                    pontos = 95000
                else:
                    pontos = int(j[0])*10000
                if j[1]=='A':
                    pontos += 99
                elif j[1]=='K':
                    pontos += 98
                elif j[1]=='Q':
                    pontos += 97
                elif j[1]=='J':
                    pontos += 96
                elif j[1]=='1':
                    pontos += 95
                else:
                    pontos += int(j[1])*10
                return pontos

            k = verifica.flush(cartas)
            if k is True:
                pontos = 10000
                return pontos

            l = verifica.Straight(cartas)
            if type(l) is int:
                pontos = l
                return pontos

            m = verifica.Trinca(cartas)
            if type(m) is not bool:
                if m=='A':
                    pontos = 95
                elif m=='K':
                    pontos = 94
                elif m=='Q':
                    pontos = 93
                elif m=='J':
                    pontos = 92
                elif m=='1':
                    pontos = 91
                else:
                    pontos = int(m)+90
                return pontos

            n = verifica.Dois_pares(cartas)
            if type(n) is list:
                if n[0]=='A':
                    pontos += 45
                elif n[0]=='K':
                    pontos += 44
                elif n[0]=='Q':
                    pontos += 43
                elif n[0]=='J':
                    pontos += 42
                elif n[0]=='1':
                    pontos += 41
                else:
                    pontos += int(n[0])+30
                if n[1]=='A':
                    pontos += 45
                elif n[1]=='K':
                    pontos += 44
                elif n[1]=='Q':
                    pontos += 43
                elif n[1]=='J':
                    pontos += 42
                elif n[1]=='1':
                    pontos += 41
                else:
                    pontos += int(n[1])+30
                return pontos

            o = verifica.Dois_pares(cartas)
            if type(o) is list:
                if o[0]=='A':
                    pontos += 55
                elif o[0]=='K':
                    pontos += 54
                elif o[0]=='Q':
                    pontos += 53
                elif o[0]=='J':
                    pontos += 52
                elif o[0]=='1':
                    pontos += 51
                else:
                    pontos = 40+int(o[0])

            p = verifica.Par(cartas)
            if type(p) is not bool:
                if p=='A':
                    pontos = 35
                elif p=='K':
                    pontos = 34
                elif p=='Q':
                    pontos = 33
                elif p=='J':
                    pontos = 32
                elif p=='1':
                    pontos = 31
                else:
                    pontos = 20+int(p)
                return pontos
            
            q = verifica.Alta(cartas)
            if type(q) is not bool:
                pontos = int(q)
                return pontos

            break










    def Royal_flush(cartas):
        if len(cartas)<5:
            return False
        ideal = [['A♠️','K♠️','Q♠️','J♠️','10♠️'],['A♣️','K♣️','Q♣️','J♣️','10♣️'],['A♦️','K♦️','Q♦️','J♦️','10♦️'],['A♥️','K♥️','Q♥️','J♥️','10♥️']]
        for a in range(4):
            conta=0
            for b in range(5):
                if ideal[a][b] in cartas:
                    conta+=1
                else:
                    break
            if conta == 5:
                return True
        return False

    def Straight_flush(cartas):
        if len(cartas)<5:
            return False
        ideal = [['9♠️','K♠️','Q♠️','J♠️','10♠️'],['9♠️','8♠️','Q♠️','J♠️','10♠️'],['9♠️','8♠️','7♠️','J♠️','10♠️'],['9♠️','8♠️','7♠️','6♠️','10♠️'],['9♠️','8♠️','7♠️','5♠️','6♠️'],['6♠️','8♠️','7♠️','5♠️','4♠️'],['3♠️','6♠️','7♠️','5♠️','4♠️'],['3♠️','6♠️','7♠️','5♠️','4♠️'],['3♠️','6♠️','2♠️','5♠️','4♠️'],['3♠️','A♠️','2♠️','5♠️','4♠️'],['9♣️','K♣️','Q♣️','J♣️','10♣️'],['9♣️','8♣️','Q♣️','J♣️','10♣️'],['9♣️','8♣️','7♣️','J♣️','10♣️'],['9♣️','8♣️','7♣️','6♣️','10♣️'],['9♣️','8♣️','7♣️','5♣️','6♣️'],['6♣️','8♣️','7♣️','5♣️','4♣️'],['3♣️','6♣️','7♣️','5♣️','4♣️'],['3♣️','6♣️','7♣️','5♣️','4♣️'],['3♣️','6♣️','2♣️','5♣️','4♣️'],['3♣️','A♣️','2♣️','5♣️','4♣️'],['9♥️','K♥️','Q♥️','J♥️','10♥️'],['9♥️','8♥️','Q♥️','J♥️','10♥️'],['9♥️','8♥️','7♥️','J♥️','10♥️'],['9♥️','8♥️','7♥️','6♥️','10♥️'],['9♥️','8♥️','7♥️','5♥️','6♥️'],['6♥️','8♥️','7♥️','5♥️','4♥️'],['3♥️','6♥️','7♥️','5♥️','4♥️'],['3♥️','6♥️','7♥️','5♥️','4♥️'],['3♥️','6♥️','2♥️','5♥️','4♥️'],['3♥️','A♥️','2♥️','5♥️','4♥️'],['9♦️','K♦️','Q♦️','J♦️','10♦️'],['9♦️','8♦️','Q♦️','J♦️','10♦️'],['9♦️','8♦️','7♦️','J♦️','10♦️'],['9♦️','8♦️','7♦️','6♦️','10♦️'],['9♦️','8♦️','7♦️','5♦️','6♦️'],['6♦️','8♦️','7♦️','5♦️','4♦️'],['3♦️','6♦️','7♦️','5♦️','4♦️'],['3♦️','6♦️','7♦️','5♦️','4♦️'],['3♦️','6♦️','2♦️','5♦️','4♦️'],['3♦️','A♦️','2♦️','5♦️','4♦️']]

        for a in range(len(ideal)):
            conta=0
            for b in range(5):
                if ideal[a][b] in cartas:
                    conta+=1
                else:
                    break
            if conta == 5:
                return ideal[a]
        return False

    def Quadra(cartas):
        conta=0
        if len(cartas)<4:
            return False
        quadra = cartas[3][0]
        for d in range(len(cartas)):
            if cartas[d][0] == quadra:
                conta+=1
        if conta == 4:
            return quadra
        return False

    def Full_House(cartas):
        if len(cartas)<5:
            return False
        combina = []
        for e in range(7):
            conta=0
            for d in range(7):
                if cartas[d][0] == cartas[e][0]:
                    conta+=1
            combina.append(cartas[e][0])
            combina.append(conta)
        
        trinca = combina.count(3)
        par = combina.count(2)        
        if trinca > 0:
            if par>0:
                full = []
                tri=combina.index(3)
                full.append(combina[tri-1])
                bi=combina.index(2)
                full.append(combina[bi-1])
                return full
        return False

    def flush(cartas):
        if len(cartas)<5:
            return False
        ideal = [['A♠️','2♠️','3♠️','4♠️','5♠️','6♠️','7♠️','8♠️','9♠️','10♠️','J♠️','Q♠️','K♠️'],['A♥️','2♥️','3♥️','4♥️','5♥️','6♥️','7♥️','8♥️','9♥️','10♥️','J♥️','Q♥️','K♥️'],['A♦️','2♦️','3♦️','4♦️','5♦️','6♦️','7♦️','8♦️','9♦️','10♦️','J♦️','Q♦️','K♦️'],['A♣️','2♣️','3♣️','4♣️','5♣️','6♣️','7♣️','8♣️','9♣️','10♣️','J♣️','Q♣️','K♣️']]
        for a in range(4):
            conta=0
            for b in range(7):
                if cartas[b] in ideal[a]:
                    conta+=1
            if conta > 4:
                return True
        return False



    def Straight(cartas):
        if len(cartas)<5:
            return False
        lista = []
        for v in range(7):
            lista.append(cartas[v][0])
        unicos = []
        for numero in lista:
            if(numero in unicos):
                pass
            else:
                unicos.append(numero)

        ideal = [['1','J','Q','K','A'],['9','1','J','Q','K'],['8','9','1','J','Q'],['7','8','9','1','J'],['6','7','8','9','1'],['5','6','7','8','9'],['4','5','6','7','8'],['3','4','5','6','7'],['2','3','4','5','6'],['A','2','3','4','5']]

        for a in range(len(ideal)):
            conta=0
            for b in range(len(unicos)):
                if unicos[b] in ideal[a]:
                    conta+=1
                if conta > 4:
                    pontos = 9999-a
                    return pontos
        return False


    def Trinca(cartas):
        if len(cartas)<3:
            return False
        combina = 0
        for e in range(len(cartas)):
            conta=0
            for d in range(len(cartas)):
                if cartas[d][0] == cartas[e][0]:
                    conta+=1
                    if conta == 3:
                        return cartas[e][0]
        return False


    def Dois_pares(cartas):
        if len(cartas)<4:
            return False
        combina = []
        for e in range(len(cartas)):
            conta=0
            for d in range(len(cartas)):
                if cartas[d][0] == cartas[e][0]:
                    conta+=1
            combina.append(cartas[e][0])
            combina.append(conta)
        par = combina.count(2)  
        if par > 2:
            full = []
            bi=combina.index(2)
            full.append(combina[bi-1])
            combina.remove(2)
            combina.remove(2)
            bi=combina.index(2)
            full.append(combina[bi-1])
            return full
        return False

    def Par(cartas):
        for e in range(len(cartas)):
            for d in range(len(cartas)):
                if cartas[d][0] == cartas[e][0]:
                    if e != d:
                        return cartas[d][0]
        return False

    def Alta(cartas):
        lista = []
        for v in range(len(cartas)):
            lista.append(cartas[v][0])
        compara = ['A','K','Q','J','1','9','8','7','6','5','4','3','2']
        for x in range(len(compara)):
            for y in range(len(lista)):
                if compara[x] == lista[y]:
                    return 15-x
        return False









#mao = ['3♦️','8♣️']
#mesa = ['10♦️']
#print(verifica.testes(mesa,mao))