import math

raio = float(input('Digite o raio de um círculo para saber a sua área: '))

area = math.pi*(raio**2)

print('A área do círculo com raio {} é igual a: {:.2f}'.format(raio, area))