#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia = float(input('Digite a distância de sua viagem: '))

if distancia <= 200:
    print('O preço de sua passagem é de: {:.2f}'.format(distancia*0.50))
else:
    print('O preço de sua passagem é de: {:.2f}'.format(distancia*0.45))