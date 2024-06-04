def piramide_diferentes(n):
    '''Concatena cada valor sem repetir'''
    for i in range(1, n + 1):
        linha = ""
        for i in range(1, i+1):
            linha += str(i) + " "
        print(linha)

n = int(input('Digite o número de linhas da pirâmide: '))
piramide_diferentes(n)