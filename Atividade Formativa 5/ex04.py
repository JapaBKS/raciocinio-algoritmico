n1 = input('Digite um número: ')
n2 = input('Digite outro número: ')
n3 = input('Digite outro número: ')

maior = n1

if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3

print(maior)