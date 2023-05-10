#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista = []

for c in range(1, 6):
    lista.append(int(input('Digite um número: ')))

maior = max(lista)
menor = min(lista)

print(f'Menor: {menor} nas posições ', end='')

for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}...', end='')

print()
print(f'Maior: {maior} nas posições ', end='')

for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}...', end='')