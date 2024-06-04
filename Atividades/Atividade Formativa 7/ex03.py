import numpy as np

linhas = 3
colunas = 2

A = []

for i in range(linhas):
    linha = []
    for j in range(colunas):
        elemento = i*j
        linha.append(elemento)
    A.append(linha)

transposta = np.array(A)
transposta = transposta.T

print(transposta)