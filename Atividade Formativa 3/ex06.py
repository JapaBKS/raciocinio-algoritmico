#Peça ao usuário para inserir um número inteiro positivo e calcule o fatorial desse
#número utilizando um loop (for).

num = int(input('Digite um número para calcular seu fatorial: '))
fat = 1

for i in range(num,1,-1):
    fat*=i
print('\nO fatorial de', num,'é igual a', fat)
print('')