peso = float(input('Digite o peso de peixes: '))

if peso > 50:
    excesso = peso - 50
    multa = excesso*4
    print('A multa de R${:.2f} deverá ser paga pelo excesso em {:.2f}kg de peixes'.format(multa, excesso))

else:
    print('O senhor não precisará pagar multa pelos {:.2f}kg de peixes pescados'.format(peso))