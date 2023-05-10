#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
#Acima de 7 Aprovado, Abaixo de 5 reprovado, entre 7 e 5 recuperação

aluno = dict()

aluno['Nome'] = input('Nome do aluno: ')
aluno['Media'] = float(input('Média do aluno: '))

if aluno['Media'] <= 5:
    aluno['Situacao'] = 'Reprovado'
elif aluno['Media'] >= 7:
    aluno['Situacao'] = 'Aprovado'
else:
    aluno['Situacao'] = 'Recuperação'

print('-' * 30)
for k, v in aluno.items():
    print(f'{k}: {v}')