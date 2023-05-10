#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = {}
gols = []

jogador['Nome'] = input('Nome: ')
jogador['Total de partidas'] = int(input('Partidas jogadas: '))

for contador in range(0, jogador['Total de partidas']):
    gols.append(int(input(f'Gols na {contador + 1}° partida: ')))

jogador['Total de gols'] = gols[:]

print('='*30)
print(jogador)

jogador['Total de gols'] = sum(gols)

print('='*30)
print()
for keys, valor in jogador.items():
    print(f'{keys}: {valor}')
print()
print('='*30)
for partida, gols in enumerate(gols):
    print(f'{partida + 1}° {jogador["Nome"]} fez: {gols}')