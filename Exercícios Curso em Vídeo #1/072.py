#Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

extenso =  ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
continuar = 'S'

while continuar in 'S':
    num = int(input('Digite um número entre 0 e 20: '))

    while num > 20 or num < 0:
        num = int(input('Opção inválida, tente novamente. Digite um número entre 0 e 20: '))

    print(f'Você digitou o núemro {extenso[num]}')

    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]