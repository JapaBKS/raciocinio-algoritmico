#Escreva um programa que solicite o salário anual de uma pessoa e determine a alíquota de imposto de renda que se aplica. 
#As alíquotas são: 0% para salário até R$ 20.000, 15% para salário entre R$ 20.001 e R$ 50.000, e 25% para salário acima de R$ 50.000.

salario_anual = float(input('Digite o seu salário anual: R$'))

if salario_anual <= 20000:
    aliquota = 0
elif salario_anual > 20000 and salario_anual <= 50000:
    aliquota = 15
else:
    aliquota = 25

print('\nPara o seu salário de R${:.2f} se aplica uma aliquota {}%.\n'.format(salario_anual, aliquota))