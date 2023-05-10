#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.


lista = []
continuar = ''


while True:
    num = int(input('Digite um valor: '))

    if num not in lista:
        print('Valor adicionado com sucesso!')
        lista.append(num)
    else:
        print('O número digitado já foi inserido anteriormente!')

    continuar = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if continuar in 'N':
        break

print(sorted(lista))
