#Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('Plano', 'Donzela', 'Beco', 'Jogos', 'Cerdas', 'Privado', 'Ensinar', 'Ansiedade')

for p in palavras:
    print(f'\nNa palavra \033[1;33m{p.upper()}\033[m temos as vogais: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print('\033[1;30m',letra.upper(), end='\033[m')