def somaImposto(taxaImposto, custo):
    '''Calcula o imposto(%) sobre o custo(R$)'''
    custo = custo + custo*(taxaImposto/100)
    return custo

preco = float(input('Digite o valor do produto: R$'))
imposto = float(input('Digite a porcentagem do imposto: '))

print(f'O preço do produto com o imposto de {imposto}% é igual a: R${somaImposto(imposto, preco)}')