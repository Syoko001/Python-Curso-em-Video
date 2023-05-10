#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

#recebendo preço
valor = float(input('Digite o valor do produto: '))

#calculo
desconto = valor - ((valor * 5) / 100) 

#print
print('Com desconto o valor final é de: R${:.2f}'.format(desconto))
