media_total = 0

for i in range(5):
    print('Aluno', i+1)
    n1 = float(input('Digite a nota 1: '))
    n2 = float(input('Digite a nota 2: '))
    n3 = float(input('Digite a nota 3: '))
    n4 = float(input('Digite a nota 4: '))

    media_aluno = (n1+n2+n3+n4)/4
    media_total += media_aluno

    if media_aluno >= 7:
        print('APROVADO! Média', media_aluno)
    else:
        print('REPROVADO! Média', media_aluno)
    i+=1
    print('')

media_total = media_total/(i)

print('A média dos', i, 'alunos é igual a', media_total)