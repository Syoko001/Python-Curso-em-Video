lista = []
par = []
impar = []

while True:
    lista.append(int(input('Digite um valor: ')))
    continuar = input('Deseja continuar? [S/N] ').upper().strip()[0]

    while continuar not in 'SN':
        print('Valor inválido, tente novamente!')
        continuar = input('Deseja continuar? [S/N] ').upper().strip()[0]
    
    if continuar in 'N':
        break

for index, valor in enumerate(lista):
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)
    
print(f'\nLista: {lista}')
print(f'Par: {par}')
print(f'Ímpar: {impar}')