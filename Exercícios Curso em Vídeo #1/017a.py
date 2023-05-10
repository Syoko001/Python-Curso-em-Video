#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
from math import pow

ca = float(input('Digite o valor de um dos catetos: '))
co = float(input('Digite o valor do outro cateto: '))

hip = (pow(ca, 2) + pow(co, 2)) ** (0.5)

print('O valor da hipotenusa de seu triângulo é {:.2f}'.format(hip))
