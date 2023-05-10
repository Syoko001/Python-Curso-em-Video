#desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média

#digite as notas de suas provas
n1 = float(input('Digite a sua nota de matemática: '))
n2 = float(input('Digite a sua nota de protuguês: '))

#calculo
media = (n1 + n2) / 2

#resultado
print('A média de suas notas é: {:.2f}'.format(media))
