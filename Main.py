from sys import exit
kjk = ['a', 'e', 'i', 'o', 'u']
a = input('Escreva uma palavra; ').lower()
contador = 0
nigga = a.replace(' ', '')

if a == 'sexo':
    print('vsfd juan kyotaka boyago')
    exit()

for text in a:
    if text in kjk:
        contador += 1

print(f'{a} tem {contador} vogais kk')