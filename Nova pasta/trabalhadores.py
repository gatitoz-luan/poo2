class trabalhadores:
    def __init__(self, id):
        self.id = id
    
    def getId(self):
        return self.id

class tecnico(trabalhadores):
    def __init__(self, id, salarioBonus):
        trabalhadores.__init__(self, id)
        self.trabalhadores = trabalhadores

class administracao(trabalhadores):
    def __init__(self, id, turno, adicionalNoturno):
        trabalhadores.__init__(self, id)
        self.turno = turno
        self.adicionalNoturno = adicionalNoturno


alberto = tecnico('2143352', 250000)

print(carlos.getId())