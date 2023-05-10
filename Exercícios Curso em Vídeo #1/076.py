#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

produtos = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

print('~'*50)
print('{:^50}'.format('\033[1mTabela de Preços\033[m'))
print('~'*50)

for count in range(0, len(produtos)):
    if count % 2 == 0:
        print(f'{produtos[count]:.<40}', end='')
    if count % 2 != 0:
        print(f'R$ {produtos[count]:>2.2f}')