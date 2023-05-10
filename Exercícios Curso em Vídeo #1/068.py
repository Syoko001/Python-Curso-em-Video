# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

ganhas = 0
jogadas = 0

while True:
    print('='*35)
    maquina = randint(0, 10)
    usuario = int(input('Quantos dedos você vais jogar? '))
    par_impar = input('Deseja par ou ímpar? [P/I] ')
    soma = maquina + usuario
    jogadas += 1

    if soma % 2 == 0 and par_impar in 'Pp':
        print('='*35)
        print(f'Você x Máquina\n {usuario}        {maquina}')
        print('PARABÉNS!!! VOCÊ GANHOU')
        ganhas += 1
    elif soma % 2 == 0 and par_impar in 'Ii':
        print('='*35)
        print(f'Você x Máquina\n {usuario}        {maquina}')
        print('INFELIZMENTE você perdeu. ;-;')
        break
    elif soma % 2 != 0 and par_impar in 'Ii':
        print('='*35)
        print(f'Você x Máquina\n {usuario}        {maquina}')
        print('PARABÉNS!!! VOCÊ GANHOU')
        ganhas += 1
    elif soma % 2 != 0 and par_impar in 'Pp':
        print('='*35)
        print(f'Você x Máquina\n {usuario}        {maquina}')
        print('INFELIZMENTE você perdeu. ;-;')
        break

print('='*35)
print(f'Você ganhou {ganhas} partidas de {jogadas}')
