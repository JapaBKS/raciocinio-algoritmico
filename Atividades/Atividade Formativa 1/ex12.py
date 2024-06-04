#Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius. C = (5 * (F-32) / 9).

farenheit = float(input('Digite uma temperatura em graus Farenheit: '))

celsius = (5*(farenheit-32)/9)

print('\nA temperatura de {:.2f}ºF em graus Celsius é igua a: {:.2f}ºC\n'.format(farenheit, celsius))