#Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(nome="<Desconhecido>", gols=0):
    return f'O jogador {nome} fez {gols} gol(s) no campeonato'


nome = input('Nome do jogador: ')
totGols = input('Gols no campeonato: ')

if totGols.isnumeric():
    totGols = int(totGols)
else:
    totGols = 0
if nome == '':
    nome = "<Desconhecido>"
print(ficha(nome, totGols))