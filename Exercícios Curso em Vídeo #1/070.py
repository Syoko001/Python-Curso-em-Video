#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.

print('='*30)
print('{:^30}'.format('Lojas Fernandão'))
print('='*30)

total = produto1000 = maisBarato = contador = 0
nomeMaisBarato = ' '

while True:
    produto = str(input('Produto: '))
    preco = float(input(f'Preços do(a) {produto}: R$'))

    contador += 1 
    total += preco

    if preco > 1000:
        produto1000 += 1
    if contador == 1:
        maisBarato = preco
        nomeMaisBarato = produto
    if maisBarato > preco:
        maisBarato = preco
        nomeMaisBarato = produto

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break

print(f'O total gasto em nossa loja foi de: R${total:.2f}')
print(f'E você comprou {produto1000} produtos que custam mais de R$1000,00.')
print(f'E o produtos mais barato que você comprou foi: {nomeMaisBarato} que custa R${maisBarato:.2f}')