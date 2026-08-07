# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostra a sua média
# ((Aula 07))

n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))

media = (n1 + n2) / 2

print('A média entre {:.1f} e {:.1f} é {:.1f}'.format(n1, n2, media))