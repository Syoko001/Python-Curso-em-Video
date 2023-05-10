#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).strip()

fraseup = frase.upper()
a = fraseup.count('A', 0)

print(a)
print(frase.find('A'))