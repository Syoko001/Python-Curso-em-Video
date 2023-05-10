#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

somaIdade = 0
maioridadehomem = 0
nomehomemvelho = ''
mulheres20anos = 0

for p in range(1, 5):
    print(f'\033[1;34m======== {p}° PESSOA ========\033[m')
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip()
    somaIdade += idade 
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomehomemvelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade 
        nomehomemvelho = nome
    if sexo in 'Ff' and idade > 20:
        mulheres20anos += 1

media = somaIdade / p
print('A média de idade do grupo é: {:.2f}'.format(media))
print('O homem mais velho do grupo é o {}, ele tem {} anos de idade.'.format(nomehomemvelho, maioridadehomem))

if mulheres20anos == 1:
    print('Apenas 1 mulher possuí mais de 20 anos.')
elif mulheres20anos > 1:
    print('{} mulheres possuem mais de 20 anos.')
else: 
    print('Nenhuma mulher possuí mais de 20 anos.')