class Pessoa:

    def __init__(self, nome = "", idade = 0):
        self.nome = nome
        self.idade = idade

    def fazer_Aniversario(self):
        self.idade += 1