#Solicite ao usuário um número inteiro e, em seguida, determine se ele é primo
#ou não utilizando um loop (for).

num = int(input('Digite um número para saber se ele é primo: '))

eh_primo = 'É primo!'

for i in range(num-1,1,-1):
    if num%i == 0:
        eh_primo = 'Não é primo!'
        break
print(eh_primo)
print('')