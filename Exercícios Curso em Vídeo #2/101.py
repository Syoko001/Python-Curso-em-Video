#Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

from datetime import date

def voto(anoNascimento):
    global idade
    idade = date.today().year - anoNascimento

    if idade >= 16 and idade < 18 or idade > 60:
        return f'Com {idade} o voto é: OPCIONAL!'
    elif idade >= 18 and idade < 60:
        return f'Com {idade} o voto é: OBRIGATÓRIO!'
    else:
        return f'Com {idade} o voto é: NEGADO!'
    

ano = int(input('Digite sua data de nascimento: '))
print(voto(ano))