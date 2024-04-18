n = int(input('Digite um número para verificar se ele é primo: '))
eh_primo = 1

for i in range(2, n):
    if n%i == 0:
        eh_primo = 0
        break
if eh_primo:
    print(f'O número {n} é primo!')
else:
    print(f'O número {n} não é primo!')