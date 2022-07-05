n = (int(input('\nDigite um número: ')),
     int(input('Digite outro número: ')),
     int(input('Digite mais um número: ')),
     int(input('Digite o último número: ')))
print(f'\nVocê digitou os números: {n}\n')
cont = 0
for c in range(0, 4):
    if n[c] == 9:
        cont += 1
if cont == 1:
    print('O número 9 apareceu 1 vez.')
else:
    print(f'O número 9 apareceu {cont} vezes.')
if 3 in n:
    print(f'O número 3 apareceu na {n.index(3)+1}° digitação.')
else:
    print('O número 3 não foi digitado.')
print('Números pares: ', end='')
for pos in n:
    if pos % 2 == 0:
        print(pos, end='  ')
    else:
        print('Nenhum foi digitado.')
        break