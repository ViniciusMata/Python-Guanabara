# Refaça o Ex_009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
# (( Aula_013 ))

num = int(input('Informe o número: '))

for c in range(0, 11):
    print('{} x {} = {}'.format(num, c, num * c))