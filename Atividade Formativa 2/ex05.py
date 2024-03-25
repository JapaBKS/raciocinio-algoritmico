#Escreva um programa que solicite ao usuário o salário atual e o tempo de serviço em anos. Se o tempo de serviço for superior a 5 anos, concede um bônus de 5% sobre o salário. Caso contrário, não conceda bônus.

salario_atual = float(input('Digite o seu salário atual: R$'))
tempo_de_serviço = float(input('Digite o tempo de serviço(em anos): ')) #6.5 anos = 6 anos e meio

if tempo_de_serviço>5:
    print('\nComo o bônus de 5%, o seu salário passa a ser R${:.2f}\n'.format(salario_atual*1.05))
else:
    print('\nO bônus não se enquadra ao seu perfil!\n')