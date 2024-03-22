#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

salario_hora = float(input('Digite o seu salário por hora trabalhada: '))
horas_trabalhadas = float(input('Digite o número de horas trabalhadas no mês: '))

salario = salario_hora*horas_trabalhadas

print('O seu salário nesse mês é igual a: {:.2f}'.format(salario))