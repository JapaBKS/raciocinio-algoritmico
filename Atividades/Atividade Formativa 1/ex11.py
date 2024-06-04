'''Faça um Programa que pergunte quanto você ganha por hora e o número
de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido
mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8%
para o INSS e 5% para o sindicato, faça um programa que nos dê:
a. salário bruto.
b. quanto pagou ao INSS.
c. quanto pagou ao sindicato.
d. o salário líquido.
e. calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Salário Bruto - Descontos = Salário Líquido.'''

salario_hora = float(input('Digite o seu salário por hora trabalhada: '))
horas_trabalhadas = float(input('Digite o número de horas trabalhadas no mês: '))

salario = salario_hora*horas_trabalhadas
imp_renda = salario*0.11
inss = salario*0.08
sindicato = salario*0.05
salario_liquido = salario-imp_renda-inss-sindicato
descontos = imp_renda+inss+sindicato


print('''\nSalário bruto: R${:.2f}\n'''
      '''\nValor pago ao IR(11%): R${:.2f}\n'''
      '''Valor pago ao INSS(8%): R${:.2f}\n'''
      '''Valor pago ao sindicato(5%): R${:.2f}\n'''
      '''Total de descontos: R${:.2f}\n'''
      '''\nSalario liquido: R${:.2f}\n'''.format(salario, imp_renda, inss, sindicato, descontos, salario_liquido))