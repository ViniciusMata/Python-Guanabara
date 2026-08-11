# Dentro do pacote utilidadesCeV que criamos no Ex_111.py, temos um módulo chamado dado. Cire uma função chamda leiaDinheiro() que seja capaz
# de funcionar como a função input(), mas com uma validação de dados para aceitar apenas valores que sejam monetários.
# (( Aula_022 ))

from utilidadesCeV import moeda
from utilidadesCeV import dado

preco = dado.leiaDinheiro('Digite o preço: R$')
moeda.resumo(preco, 20, 12)