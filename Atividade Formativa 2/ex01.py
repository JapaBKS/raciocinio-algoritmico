#Escreva um programa que solicite a nota de um aluno em uma disciplina e determine se ele foi aprovado ou reprovado. Considere que a média mínima para aprovação é 6.0.

nota = float(input('Digite a sua nota: '))

if nota >= 6:
    print('\nVocê foi aprovado!\n')
else:
    print('\nVocê foi reprovado!\n')