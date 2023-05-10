#   Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
maior = menor = 0


for c in range(0, len(numeros)):
    print(numeros[c], end=' ➔  ')
#    if c == 0:
#        maior = menor = numeros[c]
#    else:
#        if numeros[c] > maior:
#            maior = numeros[c]
#        if menor > numeros[c]:
#            menor = numeros[c]
print('FIM')

maior = max(numeros)
menor = min(numeros)

print(f'Maior: {maior}')
print(f'Menor: {menor}')
