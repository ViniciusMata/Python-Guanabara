# Modifique as funções criada no Ex_107.py e Ex_108.py para que elas aceitem um parametro a mais, informando se o valor retornado por elas vai ser 
# ou nao formatado pela funcao moeda, desenvolvido no Ex_108.py
# (( Aula_022 ))

import Moeda

preco = float(input('Digite o preço: R$'))
print(f'A metade de {Moeda.moeda(preco)} é {Moeda.metade(preco, True)}')
print(f'O dobro de {Moeda.moeda(preco)} é {Moeda.dobro(preco, True)}')
print(f'Aumentando 10%, temos {Moeda.aumentar(preco, 10, True)}')
print(f'Diminuindo 13%, temos {Moeda.diminuir(preco, 13, True)}')
