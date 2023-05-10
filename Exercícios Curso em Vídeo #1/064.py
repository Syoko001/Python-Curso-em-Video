#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

count = quant = soma = n = 0

print('\033[33m~'*35,'\033[m')

while n != 999:
    count = 0
    while count != 1:
        n = int(input('Digite um número: '))
        quant += 1
        count += 1
        soma += n

print('\033[30mVocê digitou \033[33m{}\033[30m números.\033[m'.format(quant - 1))
print('\033[30mA soma dos números que você digitou é \033[33m{}\033[30m.\033[m'.format(soma - 999))

print('\033[33m~'*35,'\033[m')