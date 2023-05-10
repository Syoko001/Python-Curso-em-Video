#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

nomec = str(input('Digite o nome de sua cidade: ')).strip()

dividido = nomec.split()
nomeM = dividido[0].upper() 

print('Analisando o nome {}!'.format(nomec))
print('Começa com SANTO: {}'.format('SANTO' in nomeM))