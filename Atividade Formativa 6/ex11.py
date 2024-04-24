lista = [1, 2, 3, 4, 5]

numero = int(input('Digite um número para remover: '))

if numero in lista:
    lista.remove(numero)

print(lista)