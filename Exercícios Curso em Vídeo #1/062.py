#Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
count = 1
termo = primeiro
termo_n = 10
total = 0 
mais = 10

while mais != 0:
    total += mais
    while count <= total:
        print(termo, '\033[30m->\033[m', end=' ')
        count += 1
        termo += razao
    print('PAUSA')
    mais = int(input('Digite quantos termos mais deseja mostrar: '))