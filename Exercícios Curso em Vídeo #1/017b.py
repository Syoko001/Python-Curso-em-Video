#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
import math

ca = float(input('Digite o valor de um dos catetos: '))
co = float(input('Digite o valor do outro cateto: '))

hip = math.hypot(ca, co)

print('O valor da hipotenusa de sua triângulo é {:.2f}'.format(hip))
