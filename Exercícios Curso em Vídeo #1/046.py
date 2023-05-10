#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep

for count in range(10, -1, -1):
    sleep(1)
    if count == 10:
        print('\033[32m{}\033[m'.format(count))
    if count == 9:
        print('\033[32m{}\033[m'.format(count))
    if count == 8:
        print('\033[32m{}\033[m'.format(count))
    if count == 7:
        print('\033[32m{}\033[m'.format(count))
    if count == 6:
        print('\033[33m{}\033[m'.format(count))
    if count == 5:
        print('\033[33m{}\033[m'.format(count))
    if count == 4:
        print('\033[33m{}\033[m'.format(count))
    if count == 3:
        print('\033[31m{}\033[m'.format(count))
    if count == 2:
        print('\033[31m{}\033[m'.format(count))
    if count == 1:
        print('\033[31m{}\033[m'.format(count))
    if count == 0:
        print('\033[31m{}\033[m'.format(count))
print('\033[1mBOOM!!!\033[m')