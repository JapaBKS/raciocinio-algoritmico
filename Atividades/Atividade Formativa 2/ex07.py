#Escreva um programa que solicite a idade de uma pessoa e determine em qual categoria ela se encaixa: criança (0-12 anos), adolescente (13-17 anos), adulto (18-59 anos) ou idoso (60 anos ou mais).

idade = int(input('Digite a sua idade: '))

if idade <= 12:
    print('\nCriança!\n')
elif idade > 12 and idade <= 17:
    print('\nAdolescente!\n')
elif idade > 17 and idade <= 59:
    print('\nAdulto!\n')
else:
    print('\nIdoso!\n')