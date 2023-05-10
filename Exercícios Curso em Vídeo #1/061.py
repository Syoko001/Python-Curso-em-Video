#Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

termo1 = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Agora digite a razão: '))
termo = termo1
count = 1
while count <= 10:
    print(termo,'\033[30m->\033[m', end=" ")
    termo += razao
    count += 1

print('FIM')