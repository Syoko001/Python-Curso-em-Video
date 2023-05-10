#Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

def contador(inicio, final, passo):
    print(f'Contagem de {inicio} até {final} de {passo} em {passo}')

    if inicio < final:
        cont = inicio
        while cont <= final:
            print(f'{cont} ', end='')
            cont += passo
        print('FIM!!!')
    else:
        cont = inicio
        while cont >= final:
            print(f'{cont} ', end='')
            cont -= passo
        print('FIM!!!')


#programa principal
contador(1, 10, 1)
contador(8, 1, 2)
print('Agora é a sua vez, digite seus próprios valores.')

while True:
    contador(int(input('Inicio: ')), int(input('Fim: ')), int(input('Razão: ')))