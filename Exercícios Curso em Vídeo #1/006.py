#crie um algoritmo que leia um número e mostre o seu dobro triplo e sua raiz quadrada

#digite um número
n = int(input('Digite um número: '))

#váriaveis
d = n * 2
t = n * 3
raiz = n ** (0.5)

#prints
print('Dobro: {}'.format(d))
print('Triplo: {}'.format(t))
print('Raiz: {}'.format(raiz))