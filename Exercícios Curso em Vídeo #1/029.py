#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

km = int(input('Digite a velocidade: '))

multa = float((km-80)*7)

if km > 80:
    print('Você foi multado no valor de R${:.2f}'.format(multa))
else: 
    print('Tudo certo')