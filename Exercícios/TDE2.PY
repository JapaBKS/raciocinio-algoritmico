lista = ['Adriel', 'Bruno', 'Carlos', 'Deivid', 'Peterson']

lista.append('Thiago')
lista.remove('Thiago')
lista[2] = 'Cleiton'

with open("arquivo.txt", "w") as arquivo:
    for nomes in lista:
        arquivo.write(nomes + '\n')