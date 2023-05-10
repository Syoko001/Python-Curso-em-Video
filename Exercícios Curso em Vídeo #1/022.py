#Crie um programa que leia o nome completo de uma pessoa e mostre:
#– O nome com todas as letras maiúsculas e minúsculas.
#– Quantas letras ao todo (sem considerar espaços).
#– Quantas letras tem o primeiro nome.

#recebendo nome
nome = str(input('Digite o seu nome: ')).strip()

print('LETRAS MAIÚSCULAS: {}'.format(nome.upper()))
print('letras minúsculas: {}'.format(nome.lower()))
print('{} letras tem o seu nome.'.format(len(nome) - nome.count(' ')))
print('{} letras tem o seu primeiro nome.'.format(nome.find(' ')))