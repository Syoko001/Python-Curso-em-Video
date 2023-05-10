#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso mostre:                                                                                                                                    
#A) Quantos números foram digitados.                                                                                                                    
#B) A lista de valores, ordenada de forma decrescente.                                                                                          
#C) Se o valor 5 foi digitado e está ou não na lista.

lista = []

while True:
    num = int(input('Digite um valor: '))
    continuar = input('Deseja continuar? [S/N] ').upper().strip()[0]
    lista.append(num)

    while continuar not in 'SN':
        print('Valor desconhecido, tente novamente')
        continuar = input('Deseja continuar? [S/N] ').upper().strip()[0]

    if continuar in 'N':
        break

if len(lista) == 1:
    print(f'Você digitou {len(lista)} número.')
else:
    print(f'Você digitou {len(lista)} números.')

lista.sort(reverse=True)
print(f'A lista em ordem decrescente é: {lista}!')

if 5 in lista:
    print('O número 5 está presente na lista.')
else:
    print('O número 5 não está presente na lista.')