#Escreva um programa que solicite ao usuário uma letra e determine se ela é uma vogal ou uma consoante. 
#(Será necessário usar o operador OU / OR, rever o material de Introdução ao Python – Operadores Lógicos).

letra = input('Digite uma letra: ')
letra = letra.upper()

if letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U':
    print('\nA letra {} é uma vogal!\n'.format(letra))
else:
    print('\nA letra {} é uma consoante!\n'.format(letra))