#Faça um programa que converta metros para centímetros.

cm = float(input('Digite um valor em cm para convertê-lo para metros: '))

metros = cm/100

print('O valor {:.2f}cm convertido para metros é igual a: {:.2f}m'.format(cm, metros))