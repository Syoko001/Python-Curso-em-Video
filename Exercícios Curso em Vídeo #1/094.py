#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
# A) Quantas pessoas foram cadastradas 
# B) A média de idade 
# C) Uma lista com as mulheres 
# D) Uma lista de pessoas com idade acima da média

temp = []
geral = []
pessoa = {}
media = 0

while True:
    pessoa['Nome'] = input('Nome: ')
    pessoa['Sexo'] = input('Sexo [F/M]: ').upper().strip()[0]
    while pessoa['Sexo'] not in 'FM':
        print('Valor inválido, tente novamente!')
        pessoa['Sexo'] = input('Sexo [F/M]: ').upper().strip()[0]
    pessoa['Idade'] = int(input('Idade: '))
    media += pessoa['Idade']

    geral.append(pessoa.copy())

    resposta = input('Deseja continuar? [S/N]: ').upper().strip()[0]
    while resposta not in 'SN':
        print('Valor inválido, tente novamente!')
        resposta = input('Deseja continuar? [S/N]: ').upper().strip()[0]
    if resposta in 'N':
        break

media /= len(geral)

print('\033[1;30m='*50, '\033[m')
print(f'A) {len(geral)} pessoas cadastradas!')
print(f'B) {media:.2f} é a média de idade do grupo!')
print('C) As mulheres cadastradas foram: ')
for index, contador in enumerate(geral):
    if geral[index]['Sexo'] in 'F':
        print(f'    {geral[index]["Nome"]}')

print('D) Essas são as pessoas com idade acima da média: ')
for index, info in enumerate(geral):
    if geral[index]['Idade'] >= media:
        print(f'    {geral[index]["Nome"]}')