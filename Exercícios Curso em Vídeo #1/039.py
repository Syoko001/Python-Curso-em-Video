#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

print('\033[1;34m-=-\033[m'*20)
print('Digite o ano de seu nascimento:')
print('\033[1;34m-=-\033[m'*20)

ano = int(input('Digite aqui: '))
idade = date.today().year - ano

if idade < 18:
    print('Ainda não está na hora de se alistar, volte em {}'.format((18 - idade) + date.today().year))
elif idade == 18:
    print('Opa, você ja possuí {} anos, então já pode fazer o seu alistamento.'.format(idade))
elif idade > 18:
    print('PERA AÍ CAMARADA, você deveria ter se alistado em {}'.format(date.today().year - (idade - 18)))
