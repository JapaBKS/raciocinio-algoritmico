#Escreva um programa que solicite a idade de uma pessoa e verifique se ela é maior de idade. 
#Se for maior de idade, verifique se tem idade suficiente para obter a Carteira Nacional de Habilitação (CNH), que é aos 18 anos no Brasil.

idade = int(input('Digite a sua idade: '))

if idade >= 18:
    print('\nVocê já tem idade para tirar a CNH!\n')
else:
    print('\nVocê ainda não tem idade para tirar a CNH!\n')