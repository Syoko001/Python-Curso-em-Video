#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('Digite um número inteiro: '))
print('''Agora escolha uma das opções abaixo:
[ 1 ] Converter o número p/ BINÁRIO.
[ 2 ] Converter o número p/ OCTAL.
[ 3 ] Converter o número p/ HEXADECIMAL.
''')
opcao = int(input('Digite a sua opção: '))

if opcao == 1:
    print('O número {} em BINÁRIO é: {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('O número {} em OCTAL é: {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('O número {} em HEXADECIMAL é: {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente.')
    