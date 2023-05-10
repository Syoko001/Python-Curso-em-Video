#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep

computador = randint(0, 5)
print('-=-'*25)
print('Estou pensando em um número entre 0 e 5... Tente adivinhar-lo.')
print('-=-'*25)
usuario = int(input('Digite aqui seu palpite: '))

print('Processando...')
sleep(1.5)
if usuario == computador:
    print('Parabéns, você acertou ^o^')
else:
    print('Puts, você errou ;-; eu pensei no {}'.format(computador))
