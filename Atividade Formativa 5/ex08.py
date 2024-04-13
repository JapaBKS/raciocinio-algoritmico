nome = input('Digite o seu nome: ')
while len(nome) < 4:
    print('Nome curto!')
    nome = input('Digite outro nome: ')

idade = int(input('Digite a sua idade: '))
while idade < 0 or idade > 150:
    print('Digite um valor entre 0 e 150!')
    idade = int(input('Digite a sua idade: '))

salario = float(input('Digite o seu salário: '))
while salario <= 0:
    print('Digite um valor maior que 0!')
    salario = float(input('Digite o seu salário: '))

sexo = input('Digite o seu sexo: ')
while sexo != 'f' and sexo != 'm':
    print("Digite 'f' ou 'm' ")
    sexo = input('Digite o seu sexo: ')

estado_civil = input('Digite o seu estado civil: ')
while estado_civil != 's' and estado_civil != 'c' and estado_civil != 'v' and estado_civil != 'd':
    print("Digite 's', 'c', 'v' ou 'd' ")
    estado_civil = input('Digite o seu estado civil: ')