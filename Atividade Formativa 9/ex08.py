def piramide_iguais(n):
    for i in range(1, n + 1):
        linha = ""
        for j in range(i):
            linha += str(i) + " "
        print(linha)

n = int(input('Digite o número de linhas da pirâmide: '))
piramide_iguais(n)