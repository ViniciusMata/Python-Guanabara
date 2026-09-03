from rich import print
from rich.panel import Panel

caixa = Panel('[white]Essa aqui é um painel de exemplo[/]:+1:', title='Mensagem', style='red', width=50)

print(caixa)