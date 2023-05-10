#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

numero = int(input('Digite um número: '))
total = 0

for c in range(1, numero+1):
    
    if numero % c == 0:
        print('\033[33m', end=' ')
        total += 1
    else:
        print('\033[30m', end= ' ')
    print('{}'.format(c), end= ' ')

if total == 2:
    print('\n\033[mSim, o número {} é PRIMO!'.format(numero))
else:
    print('\n\033[mNão, o número {} não é PRIMO!'.format(numero))
    