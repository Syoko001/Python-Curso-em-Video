#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

#recebendo valores
km = float(input('Quilômetros percorridos: '))
dias = float(input('Dias com o carro: '))

#print 
print('Valor total a ser pago: R${:.2f}'.format((km*0.15) + (dias*60)))
