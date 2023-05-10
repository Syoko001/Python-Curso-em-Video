#Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
#considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('='*30)
print('{:^30}'.format('Caixa Eletrônico'))
print('='*30)

valor = int(input('Quantos você deseja sacar? R$'))
total = valor
cedula = 50
totCedula = 0

while True:

    if total >= cedula:
        total -= cedula
        totCedula += 1
    else: 
        if totCedula != 0:
            print(f'Você receberá {totCedula} cédulas de R${cedula:.2f}')
        if cedula == 50:
            cedula = 20
            totCedula = 0 
        elif cedula == 20:
            cedula = 10
            totCedula = 0
        elif cedula == 10:
            cedula = 1
            totCedula = 0
        if total == 0:
            break