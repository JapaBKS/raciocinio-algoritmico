def fibonacci(n):
    lista = [0, 1]
    while len(lista) < n:
        prox = lista[-2] + lista[-1]
        lista.append(prox)
    return lista

n = int(input('Digite o número de elementos da lista: '))
print(fibonacci(n))