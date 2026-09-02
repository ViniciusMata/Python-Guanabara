from abc import ABC, abstractmethod
from rich import print, inspect
import random

class Personagem(ABC):
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.golpes = []

    def atacar(self, alvo, forca = 100):
        if self.vida > 0 and alvo.vida:
            golpe = self.golpes[random.randrange(0, len(self.golpes))]
            print(f"[green]{self.nome}[/][magenta]({self.vida})[/] atacou [red]{alvo.nome}[/][magenta]({alvo.vida})[/] com o golpe [blue]{golpe}[/] de força {forca}")
            alvo.receber_dano(forca)
        else:
            print(f"O ataque [green]{self.nome}[/] -> [red]{alvo.nome}[/] não pode acontecer")

    def receber_dano(self, dano):
        fator = random.randint(0, dano)
        self.vida -= fator
        if self.vida < 0:
            self.vida = 0
        print(f"[red]{self.nome}[/] recebeu [red]dano de {fator}[/]\n")

    @abstractmethod
    def curar(self):
        pass


class Guerreiro(Personagem):
    
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["Soco na Costela", "Golpe de Machado", "Pulo Giratório"]
    
    def curar(self):
        fator = random.randint(0, 100)
        self.vida += fator
        print(f"[blue]{self.nome}[/] enrolou uma atadura nos ferimentos e [green]recuperou {fator} pontos[/] de vida")


class Mago(Personagem):
    
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["Bola de fogo", "Raio de luz", "Magia Estática"]
    
    def curar(self):
        fator = random.randint(0, 100)
        self.vida += fator
        print(f"[blue]{self.nome}[/] fez uma magia de cura e [green]recuperou {fator} pontos[/] de vida")
