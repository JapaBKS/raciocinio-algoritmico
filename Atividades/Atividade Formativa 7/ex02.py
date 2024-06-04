import numpy as np

linhas = 2
colunas = 2

A = []
B = []

for i in range(linhas):
    linha = []
    for j in range(colunas):
        elemento = -i+j
        linha.append(elemento)
    A.append(linha)

for i in range(linhas):
    linha = []
    for j in range (colunas):
        elemento = -i-j
        linha.append(elemento)
    B.append(linha)

B_np = np.array(B)
A_np = np.array(A)

mult = np.dot(A_np, B_np)

print(mult)
