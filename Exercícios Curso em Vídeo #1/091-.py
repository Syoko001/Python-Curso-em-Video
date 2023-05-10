#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from operator import itemgetter

ranking = dict([])

for contador in range(1, 5):
    ranking[f'Jogador{contador}'] = randint(1, 6)
    print(f'O Jogador {contador} tirou: ',ranking[f'Jogador{contador}'])

ranking = sorted(ranking.items(), key = itemgetter(1), reverse=True)

print('-' * 30)
for index, valor in enumerate(ranking):
    print(f'{index + 1}°: {valor[0]} com {valor[1]}')