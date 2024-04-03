#Solicite ao usuário um número inteiro N e então imprima os primeiros N termos
#da sequência de Fibonacci utilizando um loop (while).

num = int(input('Digite um número para ver os N primeiros termos da sequência de Fibonacci: '))
a=0
b=1
aux = 0
i=0

while (i<num):
    print(a)
    aux = a
    a = b
    b = a+aux
    i+=1