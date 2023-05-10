# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
from math import trunc

#digite um número real
n = float(input('Digite um número real: '))

#print
print('A porção inteira de {} é {}'.format(n, trunc(n)))
