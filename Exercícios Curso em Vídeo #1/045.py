#Crie um programa que faça o computador jogar Jokenpô com você.
while True: 
    from random import randint

    print('\033[1;33m-=-\033[m'*3 + 'JOKENPÔ' + '\033[1;33m-=-\033[m'*3)
    print('''[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')
    usuario = int(input('Faça a sua escolha: '))

    maquina = randint(1,3)

    print(' \033[1;36mMáquina\033[m   x   \033[1;34mVocê\033[m')

    if maquina == 1 and usuario == 1:
        print('[ PEDRA ] x [ PEDRA ] = \033[1;30mEMPATE\033[m')
    elif maquina == 1 and usuario == 2: 
        print('[ PEDRA ] x [ PAPEL ] = \033[1;32mVOCÊ GANHOU\033[m')
    elif maquina == 1 and usuario == 3:
        print('[ PEDRA ] x [ TESOURA ] = \033[1;31mVOCÊ PERDEU\033[m')
    elif maquina == 2 and usuario == 1:
        print('[ PAPEL ] x [ PEDRA ] = \033[1;31mVOCÊ PERDEU\033[m')
    elif maquina == 2 and usuario == 2:
        print('[ PAPEL ] x [ PAPEL ] = \033[1;30mEMPATE\033[m')
    elif maquina == 2 and usuario == 3:
        print('[ PAPEL ] x [ TESOURA ] = \033[1;32mVOCÊ GANHOU\033[m')
    elif maquina == 3 and usuario == 1:
        print('[ TESOURA ] x [ PEDRA ] = \033[1;32mVOCÊ GANHOU\033[m')
    elif maquina == 3 and usuario == 2:
        print('[ TESOURA ] x [ PAPEL ] = \033[1;31mVOCÊ PERDEU\033[m')
    elif maquina == 3 and usuario == 3:
        print('[ TESOURA ] x [ TESOURA ] =\033[1;30mEMPATE\033[m')
    else:
        print('Valor inválido...')
    
    print()
    