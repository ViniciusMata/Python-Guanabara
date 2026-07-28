# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todos as informações possíves sobre ele
# ((Aula 04))

a = input('Digite algo: ')

print('O tipo primitivo desse valor é ', type(a))

print('Tem espaço ? ', a.isspace())
print('É número ? ', a.isnumeric())
print('É alfabético? ', a.isalpha())
print('É alfanumérico? ', a.isalnum())
print('Esta em maiúscula? ', a.isupper())
print('Esta em minúscula? ', a.islower())
print('Esta em capitalizada? ', a.istitle())
