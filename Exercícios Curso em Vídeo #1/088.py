#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep

print('\033[1;32m~'*50, '\033[m')
print(f"{'Palpites Mega Sena':^50}")
print('\033[1;32m~'*50, '\033[m')

jogosGerados = int(input('Quantos jogos serão gerados? '))
total = 1
lista = list()

print('Processando...')

while total <= jogosGerados:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont == 6:
            break
    
    lista.sort()
    sleep(1)
    print(f'{total}° jogo: {lista}')
    total += 1
    lista.clear()