#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#– IMC abaixo de 18,5: Abaixo do Peso
#– Entre 18,5 e 25: Peso Ideal
#– 25 até 30: Sobrepeso
#– 30 até 40: Obesidade
#– Acima de 40: Obesidade Mórbida

print('\033[1;34m-=-\033[m'*20)
peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
print('\033[1;34m-=-\033[m'*20)

imc = peso / altura ** 2 

if imc <= 18.5:
    print('Você está ABAIXO DO PESO.')
elif imc <= 25 > 18.5:
    print('Você está no peso IDEAL.')
elif imc <= 30 > 25:
    print('Você está SOBREPESO.')
elif imc <= 40 > 30:
    print('Você está OBESO.')
else:
    print('Vocé está no estágio de OBESIDADE MÓRBIDA.')
