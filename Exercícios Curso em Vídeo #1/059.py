#Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.

opcao = 0

n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))

while opcao != 5:

    print('\033[33m=-='*15, '\033[m')
    print('Agora... O que deseja fazer com esses números:')
    print('''
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa
    ''')

    opcao = int(input('Digite a opção desejada: '))

    if opcao == 1:
        soma = n1 + n2
        print('A soma de {} e {} é igual a {}!'.format(n1, n2, soma))

    elif opcao == 2:
        mult = n1 * n2
        print('A multiplicação de {} e {} é igual a {}!'.format(n1, n2, mult))

    elif opcao == 3:
        if n1 > n2: 
            print('O maior número é {}!'.format(n1))
        else:
            print('O maior número é {}!'.format(n2))

    elif opcao == 4:
        print('Você desejou, trocar os números.')
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite mais um número: '))
        opcao = 0

    elif opcao == 5:
        print('Você deseja sair do programa, até logo.')
    
    else:
        print('Opção inválida, tente novamente.')