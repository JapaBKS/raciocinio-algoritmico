import numpy as np

#Dimensões da matriz
linhas = 20
colunas = 18

#Inicializando uma matriz vazia
matriz =[]

#Preenchendo a matriz com a entrada do usuário
for i in range(linhas):
    linha = []
    for j in range(colunas):
        elemento = i*j
        linha.append(elemento)
    matriz.append(linha)

#Convertendo a lista de listas em uma lista NumPy
matriz_np = np.array(matriz)

print(matriz_np)