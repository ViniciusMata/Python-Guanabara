# Crie um pacote chamado utilidadesCeV que tenha dois modulos internos chamados moeda e dado.
# Transfira todo as funcoes utilizadas nos Ex_107.py, Ex_108.py, Ex_109.py e Ex_110.py para o primeiro pacote e mantenha tudo funcionando
# (( Aula_022 ))

from utilidadesCeV import moeda

preco = float(input('Digite o preço: R$'))
moeda.resumo(preco, 20, 12)