#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

contador = 0
boletim = list()

while True:
    boletim.append([contador])
    boletim[contador].append(input('Nome do aluno(a): '))

    for c in range(0 ,2):
        boletim[contador].append(float(input(f'{c + 1}° nota: ')))

    contador += 1
    
    continuar = input('Deseja continuar? [S/N] ').upper().strip()[0]

    while continuar not in 'SN':
        print('Valor inválido, tente novamente!')
        continuar = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if continuar in 'N':
        break

print('~' * 30)
print(f"{'Boletim':^30}")
print('~' * 30)
print()

print(f"\033[1;47m{'N':<}° {'Aluno(a)':^30} {'Média':>}\033[m")

for c in range(0, len(boletim)):
    print(f'{boletim[c][0]:<}° {boletim[c][1]:^30} {(boletim[c][2] + boletim[c][3]) / (len(boletim[c]) - 2):>.2f}')

print()
aluno = int(input('Verificar notas do aluno(a) X: [999 para sair] '))

for c in range(0, len(boletim)):
    for index, numero in enumerate(boletim[c]):
        if index == 0 and aluno == boletim[c][0]:
            print(f"\033[1;32mAluno:\033[m {boletim[c][1]} \n\033[1;32m{'Notas:'}\033[m {boletim[c][2], boletim[c][3]}")
