#faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que a cada litro de tinta, pinta uma área de 2m**2

#medidas
largura = float(input('Qual largura da sua parede? '))
altura = float(input('Qual altura da sua parede? '))

#calculo
area = largura * altura
tinta = area / 2

#print
print('Você precisa de {} latas de tinta para pintar {}m² de parede'.format(tinta, int(area)))