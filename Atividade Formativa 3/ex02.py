#Peça ao usuário para inserir um número inteiro positivo. Em seguida, some todos
#os números pares até esse limite usando um loop (while).

num = int(input('Digite um número: '))
i = 0
soma = 0

while (i<=num):
    if i%2 == 0:
        soma=soma+i
        print(i)
    i+=1

print('A soma é:', soma)