#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

cont = 's'
media = soma = count = maior = menor = 0

while cont in 'Ss':
    n = int(input('Digite um número: '))
    cont = input('Deseja continuar[S/N]?').strip()
    soma += n
    count += 1
    if count == 1:
        menor = maior = n
    if maior < n:
        maior = n
    if menor > n:
        menor = n

media = soma / count

print('A média dos números digitados é igual {:.2f}'.format(media))
print('{} foi o maior número que você digitou, e {} foi o menor.'.format(maior, menor))