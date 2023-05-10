#Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
#5! = 5 x 4 x 3 x 2 x 1 = 120

n = int(input('Digite um número: '))
resultado = n

print('{}! = '.format(n), end='')

while n != 1:
    if n != 1:
        print('{} x '.format(n), end='')
    n -= 1
    resultado = resultado * n 

if n == 1:
    print('1 = {}'.format(resultado))