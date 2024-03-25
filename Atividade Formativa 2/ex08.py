#Escreva um programa que solicite a nota de um aluno em uma prova e determine sua classificação: A (nota de 9 a 10), B (nota de 7 a 8.9), C (nota de 5 a 6.9) ou D (nota abaixo de 5).

nota = float(input('Digite a sua nota: '))

if nota >= 9:
    print('\nNota A!\n')
elif nota >= 7 and nota < 9:
    print('\nNota B!\n')
elif nota >= 5 and nota < 7:
    print('\nNota C!\n')
else:
    print('\nNota D!\n')