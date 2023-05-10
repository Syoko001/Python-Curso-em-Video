#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

princ = [[], []]
temp = []

for count in range(0, 7):
    temp.append(int(input(f'Digite o {count + 1}° valor: ')))

    if temp[0] % 2 == 0:
       princ[0].append(temp[:])
    else:
        princ[1].append(temp[:])

    temp.clear()

princ[0].sort()
princ[1].sort()

print(f'Par: {princ[0]}')
print(f'Ímpar: {princ[1]}')
