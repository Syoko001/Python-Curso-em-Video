#Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.

print('\033[33m┅\033[m'*50, '\n             Sequência de Fibonacci')
print('\033[33m┅\033[m'*50)

n = int(input('\033[30mQuantos termos deseja mostrar?\033[m '))

c = 2
termo1 = 0
termo2 = 1
termo = 0

print('\033[33m~\033[m'*50)

if n > 1:
    print('{} \033[30m➜ \033[m {}'.format(termo1, termo2), end=' \033[30m➜ \033[m ')
    while c != n:
        termo = termo1 + termo2
        print(termo, end=' \033[30m➜ \033[m ')
        termo1 = termo2
        termo2 = termo
        c += 1
    
    print('FIM')
elif n == 0:
    print('Você digitou um valor inválido')
else:
    print(termo1)