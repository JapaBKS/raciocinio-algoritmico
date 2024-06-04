nota = float(input('Digite uma nota entre 0 e 10: '))

while(nota<0 or nota>10):
    print('Digite um valor válido!')
    nota = float(input('Digite uma nota entre 0 e 10: '))