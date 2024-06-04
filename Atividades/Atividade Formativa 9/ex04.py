def soma_lista(lista):
    '''Calcula a soma dos elementos de uma lista recebida'''
    print(f'A soma da lista é igual a: {sum(lista_num)}!')

lista_num = []

for item in range(5):
    lista_num.append(int(input('Digite um número para adicionar a lista: ')))

soma_lista(lista_num)