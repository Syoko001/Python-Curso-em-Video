#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

from itertools import count


expressao = input('Digite a expressão: ')

abertos = expressao.count("(")
fechados = expressao.count(")")

if abertos == fechados:
    print('Expressão válida.')
else:
    print('Expressão inválida.')
