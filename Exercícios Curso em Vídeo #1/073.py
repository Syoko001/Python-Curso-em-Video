#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time da Chapecoense.

times = ('Flamengo', 'Palmeiras', 'Atlético Mineiro', 'Grêmio', 'Athletico Paranaense', 'Santos', 'São Paulo', 'Internacional', 'Fluminense', 'Corinthians', 'Fortaleza', 'Bahia', 'Ceará', 'Cruzeiro', 'América Mineiro', 'Atlético Goianiense', 'Chapecoense', 'Botafogo', 'Vasco da Gama', 'Red Bull Bragantino')

print('~'*35)
print('\033[1;32m{:^35}\033[m'.format('5 Primeiros colocados'))
print('~'*35)

for p in range (0, 5):
    print(f'{p+1}° ➔ ', times[p])

print('\n')
print('~'*35)
print('\033[1;31m{:^35}\033[m'.format('4 Últimos colocados'))
print('~'*35)

print('\033[1;37m...\033[m')
for p in range (16, 20):
    print(f'{p+1}° ➔ ', times[p])

print('\n')
print('~'*35)
print('\033[1;33m{:^35}\033[m'.format('Times em ordem alfabética'))
print('~'*35)

print(sorted(times))

print('\n')
print('~'*35)
print('\033[1;35m{:^35}\033[m'.format('A Chapecoense está na posição:'))
print('~'*35)

print(times.index('Chapecoense') + 1)