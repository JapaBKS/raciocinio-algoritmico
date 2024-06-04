n=1

while(n!=0):
    n = int(input('Digite um número para saber se ele é par ou ímpar (0 para sair): '))

    if n%2==0 and n != 0:
        print('O número é par!\n')
    elif n%2 != 0:
        print('O número é ímpar!\n')
    else:
        break