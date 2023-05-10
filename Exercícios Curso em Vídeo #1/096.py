# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area():
    largura = float(input('Largura do terreno: '))
    comprimento = float(input('Comprimento do terreno: '))
    print(f'A área total do terreno é {largura * comprimento} m²!')


area()
