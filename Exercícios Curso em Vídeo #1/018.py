#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math

angulo = float(input('Digite o ângulo de seu triângulo: '))

#calculos
sen = math.asin(math.radians(angulo))
cos = math.acos(math.radians(angulo))
tg = math.atan(math.radians(angulo))

print('Seno: {:.2f} Cosceno: {:.2f} Tângente: {:.2f}'.format(sen,cos,tg))
