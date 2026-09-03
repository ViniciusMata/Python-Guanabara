# Crie a classe Livro, que vai simular a passagem de páginas de um livro, considerando também se o usuario chegou ao fim da leitura

from rich import print
import time

class Livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.total_paginas = paginas
        self.pagina_atual = 1
        
        print(f':open_book: [blue]Você acabou de abrir o livro "[red]{self.titulo}[/]" que tem [green]{self.total_paginas} páginas[/] no total. \nVocê agora está na [yellow]página {self.pagina_atual}[/][/]')

    def avancar_paginas(self, qtd = 1):
        print('Lendo o livro ...')
        cont = 0
        for pg in range(0, qtd, 1):
            if not self.fim_do_livro():
                self.pagina_atual += 1
                print (f'Pág{self.pagina_atual} :arrow_forward: ', end='')
                time.sleep(0.2)
                cont += 1
        print(f'[blue]Você avaçou {cont} páginas e agora está na [yellow]página {self.pagina_atual}[/][/]')
        if self.fim_do_livro():
            print(f':closed_book:[green] Você chegou no final do livro "{self.titulo}"[/]')
        
    def fim_do_livro(self) -> bool:
        return True if self.pagina_atual == self.total_paginas else False
    
l1 = Livro('10 coisas que aprendi', 20)
l1.avancar_paginas(5)
l1.avancar_paginas(10)
l1.avancar_paginas(50)