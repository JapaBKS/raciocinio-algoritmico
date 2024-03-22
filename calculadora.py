opcao = 5

while(opcao!=0):
    opcao = int(input('''Digite uma opção: \n'''
                  '''1 - soma\n'''
                  '''2 - subtração\n'''
                  '''3 - divsão\n'''
                  '''4 - multiplicação\n'''))
    if opcao==1:
        n1 = int(input('Digite um número para somar: '))
        n2 = int(input('Digite outro número para somar: '))
        soma = n1+n2
        print('O resultado da soma é igual a {}'.format(soma))

    elif opcao==2:
        n1 = int(input('Digite um número para subtrair: '))
        n2 = int(input('Digite outro número para subtrair: '))
        sub = n1-n2
        print('O resultado da soma é igual a {}'.format(sub))

    elif opcao==3:
        n1 = int(input('Digite um número para dividir: '))
        n2 = int(input('Digite outro número para dividir: '))
        div = n1/n2
        print('O resultado da soma é igual a {}'.format(div))

    elif opcao==4:
        n1 = int(input('Digite um número para multiplicar: '))
        n2 = int(input('Digite outro número para multiplicar: '))
        mult = n1*n2
        print('O resultado da soma é igual a {}'.format(mult))
    print('\n')