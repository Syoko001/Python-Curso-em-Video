#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
from random import choice

a1 = str(input('Digite o nome de um aluno: '))
a2 = str(input('Digite o nome de um aluno: '))
a3 = str(input('Digite o nome de um aluno: '))
a4 = str(input('Digite o nome de um aluno: '))

print('O aluno escolhido foi o(a): {}'.format(choice([a1,a2,a3,a4])))
