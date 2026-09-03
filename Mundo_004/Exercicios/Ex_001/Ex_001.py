# Crie a classe Funcionarios, onde podemos cadastrar nome, setor e cargo.
# Crie também um método que permita ao funcionário se apresentar.

from rich import print
from rich import inspect

class Funcionario:
    # Atributos de Classe
    empresa = 'Curso em Vídeo'
    
    def __init__(self, nome, setor, cargo):
        # Atributos de instância
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
        
    def apresentacao(self) -> str:
        return f':handshake: Olá, sou [blue]{self.nome}[/blue] e sou {self.cargo} do setor de {self.setor} da empresa {self.__class__.empresa}'

Funcionario.empresa = 'HostNet'

c1 = Funcionario('Maria', 'Administração', 'Diretora')
print(c1.apresentacao())
#inspect(c1, methods=True)

c2 = Funcionario('Pedro', 'TI', 'Programador')
print(c2.apresentacao())
#inspect(c2, methods=True)