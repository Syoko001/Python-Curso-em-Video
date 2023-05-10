#crie um programa que leia o quanto de dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere US$1,00 = R$3,27

#recebendo os valores
real = float(input('Quantos reais você tem na carteira? '))

#calculo
dolar = real / 3.27

#print
print('Você consegue comprar US${:.2f}'.format(dolar))
