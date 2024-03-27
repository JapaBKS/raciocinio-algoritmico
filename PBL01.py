salario = float(input('Digite o seu salário: R$'))

if salario <= 2259.20:
    aliquota = 0
    parcela = 0
elif salario > 2259.20 and salario <= 2826.65:
    aliquota = 7.5
    parcela = 169.44 + (salario-2259.20)*0.075
elif salario > 2826.65 and salario <= 3751.05:
    aliquota = 15
    parcela = 381.44 + (salario-2826.65)*0.15
elif salario > 3751.05 and salario <= 4664.68:
    aliquota = 22.5
    parcela = 662.77 + (salario-3751.05)*0.15
else:
    aliquota = 27.5
    parcela = 896 + (salario-4664.68)*0.275

print('\nVocê pagará uma aliquota de {}%. Valor descontado: R${:.2f}.\n'.format(aliquota, parcela))