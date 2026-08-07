""""
Style   Text    Back    Cor
0       30      40      White
1       31      41      Red
4       32      42      Green
7       33      43      Yellow
        34      44      Blue
        35      45      Violet
        36      46      Cyan
        37      47      Gray
"""

print('\033[4;31;45mOlá, Mundo!\033[m')

a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a, b))


nome = 'Vinicius'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}

print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['pretoebranco'], nome, cores['limpa']))