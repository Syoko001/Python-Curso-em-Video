#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

listanum = []
maior = menor = count = 0

for c in range(0, 5):
    listanum.append(int(input(f'Digite o {c+1}° número: ')))

maior = max(listanum)
menor = min(listanum)

print(f'O maior número é {maior} e está na posição:', end=' ')

for index, num in enumerate(listanum):
    if num == maior:
        print(f'{index}', end='... ')

print('')
print(f'O menor número é {menor} e está na posição:', end=' ')

for index, num in enumerate(listanum):
    if num == menor:
        print(f'{index}', end='... ')
