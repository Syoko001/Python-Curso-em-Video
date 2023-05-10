#Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(*numero):
    print('Analisando os valores informados.')
    for index, valor in enumerate(numero):
        print(valor, end=' - ')
    print(f'Foram informados, {len(numero)} números ao todo.')
    print(f'Aliás o maior valor informado foi {max(numero)}')    
    print('_'*90)
    print()

maior(1, 5, 4, 3, 2, 7, 8, 9)
maior(7, 8, 1, 3, 4, 7)
maior(6)
maior(10, 21, 62, 10, 14, 98, 13)