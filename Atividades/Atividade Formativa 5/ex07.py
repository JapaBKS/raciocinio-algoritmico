n_eleitores = int(input('Digite o número de eleitores: '))

candidato_1 = 0
candidato_2 = 0
candidato_3 = 0

for n_eleitores in range (1, n_eleitores+1):
    voto = int(input('Digite o seu voto (1, 2 ou 3): '))

    if voto == 1:
        candidato_1 += 1
    elif voto == 2:
        candidato_2 += 1
    elif voto == 3:
        candidato_3 += 1

print(f'O candidato 1 teve {candidato_1} votos!')
print(f'O candidato 2 teve {candidato_2} votos!')
print(f'O candidato 3 teve {candidato_3} votos!')