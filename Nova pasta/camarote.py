class ticket:
    def __init__(self):
        self.valor = 10

class vip(ticket):
    def __init__(self):
        ticket.__init__(self)
        self.adicionaValor = 5

    def getValor(self):
        return self.valor + self.adicionaValor

class normal(ticket):
    def __init__(self):
        ticket.__init__(self)

    def getValor(self):
        return self.valor  

class camaroteInf(vip):
    def __init__(self, local):
        vip.__init__(self)
        self.local = local

    def getLocal(self):
        return self.local

class camaroteSup(vip):
    def __init__(self, local):
        vip.__init__(self)
        self.local = local
        self.adicionaValorSup = 30

    def getLocal(self):
        return self.local
    
    def getValor(self):
        return self.valor + self.self.adicionaValor + self.adicionaValorSup


ticketEspecial = camaroteSup('camarote superior')

print(ticketEspecial.getLocal())