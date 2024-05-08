def posi_neg(n):
    '''Retorna P para positivos, N para negativos ou 0'''
    if n>0:
        return 'P'
    else:
        return 'N'
    
n = int(input('Digite um número: '))
print(posi_neg(n))