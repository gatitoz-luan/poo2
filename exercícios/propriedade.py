class propriedade:
    def __init__ (self, endereco, preco):
        self.endereco = endereco
        self.preco = preco

class novo(propriedade):
    def __init__ (self, endereco, preco, precoAdicional):
        propriedade.__init__(self, endereco, preco)
        self.precoAdicional = precoAdicional

    def getPrecoAdicional(self):
        return self.precoAdicional
        
    def getPreco(self):
        return self.precoAdicional + self.preco

class velho(propriedade):
     def __init__ (self, endereco, preco):
        propriedade.__init__(self, endereco, preco)
        self.desconto = 0.15 * preco

    def getDesconto(self):
        return self.desconto
        
    def getPreco(self):
        return self.desconto + self.preco

teste = velho('rua vela encalhada', 2500000)

print(teste.getDesconto())