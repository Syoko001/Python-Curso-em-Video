#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

usuario = int(input('Estou pensando em um número\033[30m(inteiro)\033[m de 0 a 10. Tente adivinhá-lo: '))
pc = randint(0, 10)
tentativas = 1

while pc != usuario:
    if usuario < pc:
        usuario = int(input('Mais...\033[31mVocê errou\033[m, tente novamente: '))
    if usuario > pc:
        usuario = int(input('Menos...\033[31mVocê errou\033[m, tente novamente: '))    
    tentativas += 1
    if usuario == pc:
        print('Você \033[1;34mACERTOU\033[m!')

print('Você tentou {} vezes.'.format(tentativas))