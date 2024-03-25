#Escreva um programa que leia um número inteiro e determine se ele é positivo, negativo ou zero.

num = int(input('Digite um número: '))

if num > 0:
    print('\nO número é positivo!\n')
elif num < 0:
    print('\nO número é negativo!\n')
else:
    print('\nO número é igual a zero!\n')