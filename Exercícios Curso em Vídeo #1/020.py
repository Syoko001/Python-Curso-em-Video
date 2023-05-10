#O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import sample

a1 = str(input('Digite o nome de um aluno: '))
a2 = str(input('Digite o nome de um aluno: '))
a3 = str(input('Digite o nome de um aluno: '))
a4 = str(input('Digite o nome de um aluno: '))

print('A ordem de apresentação é: {}'.format(sample([a1, a2, a3, a4],4)))
