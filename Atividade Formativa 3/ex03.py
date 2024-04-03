#Solicite ao usuário um número inteiro. Após isso, imprima a tabuada
#correspondente a esse número de 1 a 10 utilizando um loop (for).

num = int(input('Digite um número para visualizar sua tabuada: '))

for i in range(10):
    print(i+1, 'x', num, '=', (i+1)*num)
    i+=1