#Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(num, show=False):
    """
    num: Número que deseja descobrir o fatorial
    show: se True mostra a conta, se False só mostra o resultado 
    """
    result = 1
    print('='*40)
    if show == True:
        for contagem in range(num, 1, -1):
            print(contagem, end=' x ')
            result *= contagem
        print(f'1 = {result}')
    else:
        for contagem in range(num, 0, -1):
            result *= contagem
        print(result)

fatorial(9, True)
help(fatorial)