#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

print('~'*20)
print('\033[33mTabuada\033[m')
print('~'*20)


while True:
    n = int(input('Quer ver a tabuada de qual número? '))
    print('~'*20)
    if n < 0:
        break
    else:
        for c in range (1, 11):
            print(f'{n} x {c} = {n*c}')
        print('~'*20)
print('Acabou!')