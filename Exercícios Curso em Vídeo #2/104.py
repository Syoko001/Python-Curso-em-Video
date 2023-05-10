#Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

def leiaInt(texto):
    ok = False
    num = input(texto)
    while True:
        if num.isnumeric():
            ok = True
            print(num)
        else:
            return '\033[1;31mERRO!!! O valor digitado não é um número. Tente novamente.'
        if ok == True:
            break


leiaInt('Digite um número: ')
