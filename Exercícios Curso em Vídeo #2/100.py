#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint

numeros = []


def sorteia():
    for contador in range(0, 5):
        numeros.append(randint(0, 9))
    print(f'Os números aleatorizados foram {numeros}')
    

def somaPar():
    soma = 0
    for valor in numeros:
        if valor % 2 == 0:
            soma += valor
    print(f'A soma dos valores aleatorizados é {soma}')

sorteia()
somaPar()