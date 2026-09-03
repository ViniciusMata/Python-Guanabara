from rich import print
from rich.table import Table

tabela = Table(title='Tabela de Preço')

tabela.add_column('Nome', justify='left')
tabela.add_column('Preço', justify='left')

tabela.add_row('Lápis', 'R$1,00')
tabela.add_row('Borracha', '[green]R$2,00[/]')

print(tabela)