import numpy as np

linhas = 4
colunas = 4

A = []

for i in range(linhas):
    linha = []
    for j in range(colunas):
        elemento = i*i
        linha.append(elemento)
    A.append(linha)

np_A = np.array(A)

print(np_A)