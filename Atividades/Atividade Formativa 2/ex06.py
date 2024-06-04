#Escreva um programa que solicite ao usuário o valor da compra e verifique se ele tem direito a um desconto. Se o valor da compra for maior que R$ 100,00, conceda um desconto de 10%. Caso contrário, não conceda desconto.

compra = float(input('Digite o valor da compra: R$'))

if compra > 100:
    print('\nVocê tem direito a um desconto de 10%. Valor final: R${:.2f}\n'.format(compra*0.9))

else:
    print('\nVocê não tem direito ao desconto. Valor final: R${:.2f}\n'.format(compra))