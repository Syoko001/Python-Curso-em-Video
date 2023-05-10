#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#– EQUILÁTERO: todos os lados iguais
#– ISÓSCELES: dois lados iguais, um diferente
#– ESCALENO: todos os lados diferentes

print('\033[1;034m-=-\033[m'*20)
r1 = float(input('Digite a primeira reta: '))
r2 = float(input('Digite a segunda reta: '))
r3 = float(input('Digite a terceira reta: '))
print('\033[1;034m-=-\033[m'*20)

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Sim, elas formam um triângulo')
    if r1 == r2 == r3:
        print('Formam um triângulo EQUILÁTERO.')
    elif r1 != r2 == r3 and r2 != r1 == r3 and r3 != r1 == r2:
        print('Formam um triângulo ISÓSCELES.')
    elif r1 != r2 != r3:
        print('Formam um triângulo ESCALENO.')
else:
    print('Elas não formam um triângulo.')
