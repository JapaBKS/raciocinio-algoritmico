#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

lado = float(input('Digite o valor do lado do quadrado: '))

area = lado**2

print('A área do quadrado de lado {:.2f} é igual a {:.2f} e o dobro é igual a {:.2f}'.format(lado, area, area*2))