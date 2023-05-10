#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#– Até 9 anos: MIRIM
#– Até 14 anos: INFANTIL
#– Até 19 anos: JÚNIOR
#– Até 25 anos: SÊNIOR
#– Acima de 25 anos: MASTER

from datetime import date

print('\033[1;34m-=-\033[m'*35)
ano = int(input('Digite o ano em que você nasceu: '))

idade = date.today().year - ano 

if idade < 9:
    print('Você possuí {} anos, portanto se encaixa na categoria MIRIM.'.format(idade))
elif idade <= 14 and idade > 9:
    print('Você possuí {} anos, portanto se encaixa na categoria INFANTIL.'.format(idade))
elif idade <= 19 and idade > 14:
    print('Você possuí {} anos, portanto se encaixa na categoria JÚNIOR.'.format(idade))
elif idade <= 25 and idade > 19:
    print('Você possuí {} anos, portanto se encaixa na categoria SÊNIOR.'.format(idade))
elif idade >= 25:
    print('Você possuí {} anos, portanto se encaixa na categoria MASTER.'.format(idade))
