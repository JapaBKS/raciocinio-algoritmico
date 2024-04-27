vetor = []

while True:
    opcao = int(input('Digite 1 para adicionar, 0 para remover um elemento e outro para sair: '))
    if opcao == 1:
        adiciona = input('Digite um valor para adicionar ao vetor: ')
        vetor.append(adiciona)
    elif opcao == 0:
        remove = input('Digite um valor para remover do vetor: ')
        vetor.remove(remove)
    else:
        break

vetor.sort()
print(vetor)