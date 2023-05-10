#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

print('\033[1;34m=\033[m'*50, '\nOS 10 TERMOS DE UMA PA','\n','\033[1;34m=\033[m'*50)


termo1 = int(input('Digite o termo de uma PA: '))
razao = int(input('Digite a razão da mesma: '))

decimo = termo1 + (10-1) * razao

for n in range(termo1, decimo + razao, razao):
    print('{} '.format(n), end='> ')
print('Acabou')