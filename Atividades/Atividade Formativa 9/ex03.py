def maximo(n1, n2):
    '''Escreve o maior número dentre os dois recebidos (ou se forem iguais)'''
    if n1>n2:
        print(f'O número {n1} é maior!')
    elif n2>n1:
        print(f'O número {n2} é maior!')
    else:
        print('Os números são iguais!')

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
maximo(n1, n2)