#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import date

pessoa = dict()

pessoa['Nome'] = input('Nome: ')
pessoa['Idade'] = date.today().year - int(input('Data de nascimento: '))
pessoa['Carteira de Trabalho'] = int(input('Carteira de trabalho [0 se não tem]: '))
if pessoa['Carteira de Trabalho'] != 0:
    pessoa['Ano de contratação'] = int(input('Ano de contratação: '))
    pessoa['Salário'] = float(input('Salário: R$'))
    pessoa['Aposentadoria'] = pessoa['Idade'] + ((pessoa['Ano de contratação'] + 35) - date.today().year)

print('~' * 30)

for key, valor in pessoa.items():
    print(f'{key}: {valor}')