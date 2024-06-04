nome = input('Digite o seu nome: ')
senha = input('Digite a sua senha: ')

while senha == nome:
    print('Senha inválida!')
    nome = input('Digite o seu nome: ')
    senha = input('Digite a sua senha: ')