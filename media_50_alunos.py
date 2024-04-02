media_total = 0
i = 1

while(i<=5):
    print('Aluno', i)
    n1 = float(input('Digite a nota 1: '))
    n2 = float(input('Digite a nota 2: '))
    n3 = float(input('Digite a nota 3: '))
    n4 = float(input('Digite a nota 4: '))

    media_aluno = (n1+n2+n3+n4)/4
    media_total = media_total + media_aluno

    if media_aluno >= 7:
        print('APROVADO! Média', media_aluno)
    else:
        print('REPROVADO! Média', media_aluno)
    i+=1
    print('')

media_total = media_total/(i-1)

print('A média dos', i-1, 'alunos é igual a', media_total)