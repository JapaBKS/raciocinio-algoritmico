#Escreva um programa que solicite ao usuário os três lados de um triângulo e determine se ele é equilátero, isósceles ou escaleno.

l1 = float(input('Digite o primeiro lado do triângulo: '))
l2 = float(input('Digite o segundo lado do triângulo: '))
l3 = float(input('Digite o terceiro lado do triângulo: '))

if l1!=l2 and l2!=l3:
    print('\nO triângulo é escaleno!\n')
elif l1==l2 and l2==l3:
    print('\nO triângulo é equilátero!\n')
else:
    print('\nO triângulo é isósceles!\n')