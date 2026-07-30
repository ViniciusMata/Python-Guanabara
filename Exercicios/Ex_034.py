# Escreva um program que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.
# ((Aula 10))

salario = float(input('Digite o salário do funcionário: R$'))

if salario > 1250:
    aumento = salario * 0.10
else:
    aumento = salario * 0.15

print('O aumento do salário será de R${:.2f}'.format(aumento))