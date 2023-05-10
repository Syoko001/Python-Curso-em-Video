#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal 
#– 3x ou mais no cartão: 20% de juros

print('\033[1;33m-=-\033[m'*3 + 'LOJAS MURILLINHO' + '\033[1;33m-=-\033[m'*3)

valor = float(input('Digite o \033[33mvalor\033[m de suas compras: R$'))

print('Agora selecione a \033[33mforma de pagamento\033[m:')

print('''[ 1 ] à vista \033[30m(Dinheiro ou Cheque)\033[m
[ 2 ] à vista no cartão
[ 3 ] em até 2x no cartão
[ 4 ] 3x ou mais no cartão: 20% de juros''')

opcao = int(input('Digite a opção que deseja: '))
print('\033[1;33m-=-\033[m'*30)
#============================================================================================================

if opcao == 1:
    print('''À VISTA você recebe um desconto de 10%
    Então de R${:.2f} você pagará R${:.2f}'''.format(valor, valor - (valor * 0.10)))
elif opcao == 2:
    print('''À VISTA NO CARTÃO você recebe 5% de desconto
    Então de R${:.2f} você pagará R${:.2f}'''.format(valor, valor - (valor * 0.05)))
elif opcao == 3:
    print('2x NO CARTÃO, o valor a ser pago é R${:.2f}'.format(valor))
elif opcao == 4:
    parcelas = int(input('Digite o número de parcelas: '))
    print('''3x OU MAIS NO CARTÃO, você pagará um total de R${:.2f}
    com parcelas de R${:.2f} mensais.\033[30m(Juros adicionados)\033[m'''.format(valor + (valor * 0.20), ((valor * 0.20) + valor)/parcelas))
else: 
    print('TRANSAÇÃO INVÁLIDA, TENTE NOVAMENTE.')