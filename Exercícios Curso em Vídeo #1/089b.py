ficha = []

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('1° Nota: '))
    nota2 = float(input('2° Nota: '))
    media = (nota1 + nota2) / 2 
    ficha.append([nome, [nota1, nota2], media])

    continuar = input('Deseja continuar? [S/N]: ')
    while continuar not in 'SNsn':
        continuar = input('Deseja continuar? [S/N]: ')
    if continuar in 'Nn':
        break

print('~'*30)
print(f'{"BOLETIM":^30}')
print('~'*30)
print(f'{"N.":<5}{"NOME":^20}{"MÉDIA":>}')
print('-'*30)

for index, info in enumerate(ficha):
    print(f'{index:<5}{info[0]:^20}{info[2]:>.2f}')

while True:
    opcao = int(input('Deseja mostrar qual aluno? (999 interrompe): '))
    if opcao == 999:
        break
    if opcao <= len(ficha) - 1:
        print(f'O aluno(a) {ficha[opcao][0]} tirou {ficha[opcao][1]}')