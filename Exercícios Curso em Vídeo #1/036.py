#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
from time import sleep


print('\033[1;34m-=\033[m'*20)
print('\033[1;37m...Aprovador de Empréstimo bancário...\033[m')
print('\033[1;34m-=\033[m'*20)

casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Agora digite o seu salário: R$'))
anos = float(input('Em quantos anos pretende terminar de pagar a divida ?'))

prestacao = casa / (anos * 12)
minimoSalario = salario * 0.30

print('-'*20)
print('Processando...')
print('-'*20)
sleep(2)

print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}...'.format(casa, anos, prestacao))
if prestacao > minimoSalario:
    print('\033[31mINFELIZMENTE o seu empréstimo foi negado...\033[m')
else:
    print('\033[32mOBA, seu empréstimo foi ACEITO! \033[0;34m^_^\033[m')