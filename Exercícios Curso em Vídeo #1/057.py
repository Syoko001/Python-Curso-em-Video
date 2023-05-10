# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

s = 1
while s != 0:
    sexo = input('Digite seu sexo [M/F]: ').upper()
    if sexo == 'M' or sexo == 'F':
        s = 0
    else:
        print('Sexo inválido, digite novamente.')

if sexo == 'M':
    print('Olá senhor.')
elif sexo == 'F':
    print('Olá senhora.')
