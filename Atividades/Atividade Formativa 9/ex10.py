def fibonacci(n):
    '''Exibe os n primeiros termos da sequência de Fibonacci'''
    lista = [0, 1] #inicializa uma lista com os dois primeiros valores da sequência
    while len(lista) < n:
        prox = lista[-2] + lista[-1] #o próximo recebe o valor da soma do último com o antepenúltimo valor da lista 
        lista.append(prox) #adiciona o próximo valor na lista
    return lista

n = int(input('Digite o número de elementos da lista: '))
print(fibonacci(n))