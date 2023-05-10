#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.

numeros = (int(input('Digite um número: ')), 
int(input('Digite um número: ')), 
int(input('Digite um número: ')), 
int(input('Digite um número: ')))

print(f'O número 9 apareceu {numeros.count(9)} vezes')
if numeros.count(3) > 0:
    print(f'A primeira posição do número 3 foi: {numeros.index(3) + 1}')
else:
    print('Nenhum número 3 foi digitado.')

print('Os núemros pares digitados foram: ', end='')
for c in range (0, len(numeros)):
    if numeros[c] % 2 == 0:
        print(numeros[c], end=' ')