#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date

maior_Idade = 0
menor_Idade = 0
for c in range(1, 8):
    atual = date.today().year
    nascimento = int(input('Digita a data de nascimento da {}° pessoa: '.format(c)))
    idade = atual - nascimento
    if idade >= 21:
        maior_Idade += 1
    else:
        menor_Idade += 1

print("{} pessoas, são maiores de idade.".format(maior_Idade))
print("{} pessoas, são menores de idade.".format(menor_Idade))