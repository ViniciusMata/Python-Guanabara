# Crie a classa Gamer, ond epodemos cadastrar nome, nick e os jogos favoritos de uma pessoa. Crie também um método que permita mostrar a ficha desse gamer.

from rich import print
from rich.panel import Panel

class Gamer:
    
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.favoritos = list()
    
    def add_favoritos(self, game):
        self.favoritos.append(game)
        self.favoritos = sorted(self.favoritos, key=str.lower)
    
    def ficha(self):
        conteudo = f'Nome real: [black on blue] {self.nome} [/]'
        conteudo += f'\nJogos favoritos:'
        for num, game in enumerate(self.favoritos):
            conteudo += f'\n:video_game: [blue]{game}[/]'
        painel = Panel(conteudo, title=f'Jogador <{self.nick}>', width=40)
        print(painel)

j1 = Gamer('Vinicius Mata', 'viniMata')
j1.add_favoritos('Mario Bros')
j1.add_favoritos('Sonic')
j1.add_favoritos('God of War')
j1.add_favoritos('Fortnite')
j1.ficha()

j2 = Gamer('Lucas Mata', 'lucasMata')
j2.add_favoritos('Fifa 26')
j2.add_favoritos('COD')
j2.add_favoritos('GTA VI')
j2.ficha()