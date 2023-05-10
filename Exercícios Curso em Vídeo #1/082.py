#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista = []
lista_par = []
lista_impar = []

while True:
    num = int(input('Digite um valor: '))
    continuar = input('Deseja continuar? [S/N] ').upper().strip()[0]

    lista.append(num)

    if num % 2 == 0:
        lista_par.append(num)
    else:
        lista_impar.append(num)


    while continuar not in 'SN':
        print('Valor inválido, tente novamente!')
        continuar = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if continuar in 'N':
        break

print('\033[33m=-'*30, '\033[m')
print(f'Eis os números digitados:\n{lista}')
print(f'Esses são os números pares: {lista_par}')
print(f'Esses são os números ímpares: {lista_impar}')