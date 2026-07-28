# importa todas as funcionalidades
import math
import random
import emoji

# importa somente a funcionalidade
from math import sqrt, ceil, floor

#num = int(input('Digite um número: '))
num = random.randint(1, 100)

raiz = math.sqrt(num)

# ceil arredonda para cima
# floor arredonda para baixo

print('A raiz de {} é {:.2f}'.format(num, raiz))

print(emoji.emojize("Python é :polegar_para_cima:", language='pt'))