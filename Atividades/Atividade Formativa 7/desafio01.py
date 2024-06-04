import numpy as np

linhas = 2
colunas = 2

A = []

for i in range(linhas):
    linha = []
    for j in range(colunas):
        elemento = i*j
        linha.append(elemento)
    A.append(linha)

matriz = np.array(A)
transposta = matriz.T

print(matriz)
print(transposta)

print(np.array_equal(matriz, transposta))