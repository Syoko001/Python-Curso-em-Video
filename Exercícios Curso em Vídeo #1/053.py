#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

frase = str(input('Digite um frase aqui: ')).strip().replace(' ', '').upper()

invertida = frase[::-1]

if frase == invertida:
    print('''Sim a frase,
\033[34m{}\033[m
É um PALÍNDROMO.'''.format(frase))
else:
    print('''A frase,
\033[34m{}\033[m
NÃO é um PALÍNDROMO.'''.format(frase))