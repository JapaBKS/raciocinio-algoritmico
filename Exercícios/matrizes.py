import numpy as np

#Criando um array a partir de uma lista
arr = np.array([1, 2, 3, 4, 5])

#Criando um array a partir de uma lista
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

#Criando um array de zeros
zeros = np.zeros((2, 3)) #2 linhas, 3 colunas

#Criando um array de uns
uns = np.ones((2, 3)) #2 linhas, 3 colunas

#Criando uma matriz identidade
identidade = np.eye((3)) #matriz identidade 3x3

#Multiplicação de matrizes
A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])

mult = np.dot(A, B)

#Transpondo matriz (linhas viram colunas)
transp = np.array([[1, 2, 3],
                   [4, 5, 6],])

transp = transp.T

print(arr)
print('')
print(matrix)
print('')
print(zeros)
print('')
print(uns)
print('')
print(identidade)
print('')
print(mult)
print('')
print(transp)