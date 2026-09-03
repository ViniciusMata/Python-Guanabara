# Declaração de Classe
class Gafanhoto:
    # Método Construtor
    def __init__(self):
        
        # Atributos de Instancia
        self.nome = ""
        self.idade = 0

    # Métodos de Instancia
    def aniversaio(self):
        self.idade = self.idade + 1

    def mensagem(self):
        return f'{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade.'

# Declaração de Objetos
g1 = Gafanhoto()
g1.nome = 'Vinícius'
g1.idade = 32
g1.aniversaio()
print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = 'Stephanie'
g2.idade = 29
g2.aniversaio()
print(g2.mensagem())

g3 = Gafanhoto()
g3.nome = 'Lucas'
g3.idade = 2
g3.aniversaio()
print(g3.mensagem())