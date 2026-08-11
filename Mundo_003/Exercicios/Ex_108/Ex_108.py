# Adapte o código do Ex_107.py, criando uma função adicional chamda moeda() que consiga mostrar os valores como um valor monetário formatado.
# (( Aula_022 ))

import Moeda

preco = float(input('Digite o preço: R$'))
print(f'A metade de {Moeda.moeda(preco)} é {Moeda.moeda(Moeda.metade(preco))}')
print(f'O dobro de {Moeda.moeda(preco)} é {Moeda.moeda(Moeda.dobro(preco))}')
print(f'Aumentando 10%, temos {Moeda.moeda(Moeda.aumentar(preco, 10))}')