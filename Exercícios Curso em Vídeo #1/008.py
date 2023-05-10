#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

#digite um valor
metros = float(input('Digite o valor em metros: '))

#calculos
decimetro = metros * 10
centimetros = metros * 100
milimetros = metros * 1000
quilometro = metros / 1000
hectometro = metros / 100
decametro =  metros / 10

#print
print('{} metros em dm: {}'.format(metros, decimetro))
print('{} metros em cm: {}'.format(metros, centimetros))
print('{} metros em mm: {}'.format(metros, milimetros))
print('{} metros em km: {}'.format(metros, quilometro))
print('{} metros em hm: {}'.format(metros, hectometro))
print('{} metros em dam: {}'.format(metros, decametro))