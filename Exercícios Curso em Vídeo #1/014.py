#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

#recebendo temperatura em °C
c = int(input('Digite a temperatura em °C: '))

#calculo
f = (c/5) * 9 + 32

#print
print('{}°C em fahrenheit é igual a: {:.1f}°F'.format(c, f))
