# Declaração de Classe
class Gafanhoto:
    """_summary_
        Essa classe cria um gafanhoto, que é uma pesso que tem nome e idade
        Para criar uma pesosa, use:
        Variavavel = Gafanhoto(nome, idade)
    """
    # Método Construtor
    def __init__(self, nome="", idade=0):
        # Atributos de Instancia
        self.nome = nome
        self.idade = idade

    # Métodos de Instancia
    def aniversaio(self):
        self.idade = self.idade + 1

    def __str__(self):  # Dunder Method
        return f'{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade.'

    def __getstate__(self):
        return f'Estado: nome = {self.nome} ; idade = {self.idade}'

# Declaração de Objetos
g1 = Gafanhoto("João", 32)
g1.aniversaio()
print(g1)

print(g1.__doc__) # Dunder Attribute
print(g1.__dict__) # Dunder Attribute
print(g1.__class__) # Dunder Attribute 
print(g1.__getstate__()) # Dunder Method