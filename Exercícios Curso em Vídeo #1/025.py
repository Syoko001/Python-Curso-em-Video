#Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = str(input('Digite seu nome: ')).strip()

print('Analisando o nome {}!'.format(nome))
print('Possuí SILVA no nome: {}'.format('SILVA' in nome.upper()))