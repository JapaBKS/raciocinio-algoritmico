#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula:

altura = float(input('Digite a sua altura em metros: '))

imc = (72.7*altura)-58

print('Com base na sua altura, o seu peso ideal é de: {:.2f}kg'.format(imc))