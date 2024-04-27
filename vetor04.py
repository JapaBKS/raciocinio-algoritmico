vetor = [7, 5, 1, 8, 4, 9, 6, 2, 3, 10]

vetor.sort()

print(vetor)

n = int(input('Digite um valor para pesquisar: '))

if n in vetor:
    print(f'O valor está presente na posição {vetor.index(n)}')
else:
    print('O valor não está presente no vetor')