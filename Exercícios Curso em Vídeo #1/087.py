#Aprimore o desafio anterior, mostrando no final:                                                    
# A) A soma de todos os valores pares digitados.                                                                                                 
#B) A soma dos valores da terceira coluna.                                                                                                                
# C) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_par = soma_coluna = maior = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um número para [{linha}, {coluna}]: '))

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end= '')

        if matriz[linha][coluna] % 2 == 0:
            soma_par += matriz[linha][coluna]
        
        if coluna == 2:
            soma_coluna += matriz[linha][coluna]

        if linha == 1:
            maior = max(matriz[linha])


    print()

print(f'A soma dos números pares da matriz é: {soma_par}!')
print(f'A soma dos valores da terceira coluna é: {soma_coluna}')
print(f'O maior valor da segunda linha é: {maior}')