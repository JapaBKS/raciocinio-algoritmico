def media(n1, n2, n3):
    '''Calcula a média entre 3 número recebidos'''
    media = (n1+n2+n3)/3
    print(f'A média entre os 3 números é igual a: {media}')

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite outro número: '))

media(n1, n2, n3)

help(media)