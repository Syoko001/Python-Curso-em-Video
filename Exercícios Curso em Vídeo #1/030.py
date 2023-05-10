#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

n = int(input('Digite um número: '))
resultado = n % 2

if resultado == 1:
    print('O número {} é ÍMPAR'.format(n))
else:
    print('O número {} é PAR'.format(n))

