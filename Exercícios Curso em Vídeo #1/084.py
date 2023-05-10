# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:                                                                                                    
#A) Quantas pessoas foram cadastradas.                                                                                                                
#B) Uma listagem com as pessoas mais pesadas.                                                                                                    
#C) Uma listagem com as pessoas mais leves.

cadastros = []
pessoas = []
count = pesada = leve = 0

while True:
    pessoas.append(input('Nome: '))
    pessoas.append(int(input('Peso: ')))
    cadastros.append(pessoas[:])
    
    count += 1

    if count == 1:
        pesada = leve = pessoas[1]

    else:
        if pessoas[1] > pesada:
            pesada = pessoas[1]

        if pessoas[1] < leve:
            leve = pessoas[1]

    pessoas.clear()

    continuar = input('Deseja continuar? [S/N] ').upper().strip()[0]

    while continuar not in 'SN':
        print('Valor inválido, tente novamente!')
        continuar = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if continuar in 'N':
        break

print('\033[1;33m='*30, '\033[m')
print(f'{len(cadastros)} pessoas cadastradas.')

print(f'As pessoas mais pesadas tem {pesada}KG e são:', end=' ')
for pessoa in cadastros:
    if pessoa[1] == pesada:
        print(f'{pessoa[0]}', end=' ')

print()
print(f'As pessoas mais leves tem {leve}KG e são:', end=' ')
for pessoa in cadastros:
    if pessoa[1] == leve:
        print(f'{pessoa[0]}', end=' ')