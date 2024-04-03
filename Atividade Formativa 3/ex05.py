#Peça ao usuário para fornecer uma lista de números e então calcule a média
#desses números utilizando um loop (for).

tam_lista = int(input('Digite a quantidade de números para calcular a média: '))
lista_numeros = []
media = 0

for i in range(tam_lista):
    num = float(input('Digite o {}º número: '.format(i+1)))
    lista_numeros.append(num)
    media+=num/tam_lista

print('\nA média dos',tam_lista,'números é igual a',media)
print(lista_numeros)