#Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

jogador = dict()
tot_gols = list()
galera = list()

while True:
    jogador['Nome'] = input('Nome do jogador: ')
    jogador['Tot_partidas'] = int(input(f'Total de partidas que \033[33m{jogador["Nome"]}\033[m jogou: '))
    for partidas in range(0, jogador['Tot_partidas']):
        tot_gols.append(int(input(f'    \033[30mQuantos gols fez na {partidas + 1}° partida: \033[m')))
    jogador['Gols'] = tot_gols[:]
    jogador['Tot_gols'] = sum(tot_gols)
    tot_gols.clear()

    galera.append(jogador.copy())
    jogador.clear()

    resposta = input('Deseja continuar? [S/N]: ').upper().strip()[0]
    while resposta not in 'SN':
        print('Valor inválido, tente novamente!')
        resposta = input('Deseja continuar? [S/N]: ').upper().strip()[0]
    if resposta in 'N':
        break

print('\033[1m=-'*30, '\033[m')
print(f'\033[1m{"N°":5<}{"Jogadores":^20}{"Gols":^20}{"Total de Gols":>5}\033[m')
print('-'*60)

for contador in range(0, len(galera)):
    print(f'{contador:5<}{galera[contador]["Nome"]:^20}{str(galera[contador]["Gols"]):^20}{galera[contador]["Tot_gols"]:>5}')

while True:
    busca = int(input('Pesquise por um jogador [999 interrompe]: '))
    if busca == 999:
        break
    print()
    print('~'*60)
    print(f'\033[1;mLevantamento do(a) jogador(a) {galera[busca]["Nome"]}:\033[m')
    for contador, gols in enumerate(galera[busca]["Gols"]):
        print(f'  ➜  Na {contador + 1}° fez {gols} Gol(s)!')
