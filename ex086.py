matriz = []
somapar = soma3 = maior2 = 0
for n in range(0, 3):
    matriz.append(int(input(f'Digite um valor para [0,{n}]: ')))
for n in range(0, 3):
    matriz.append(int(input(f'Digite um valor para [1,{n}]: ')))
for n in range(0, 3):
    matriz.append(int(input(f'Digite um valor para [2,{n}]: ')))
print('\n{:^15}\n'.format('MATRIZ 3X3'))
cont = 0
for n in matriz:
    print(f'[ {n} ]', end='')
    cont += 1
    if cont % 3 == 0:
        soma3 += n
        print('')
    if 6 >= cont >= 4:
        if cont == 4:
            maior2 = n
        else:
            if n > maior2:
                maior2 = n
    if n % 2 == 0:
        somapar += n
print('\n{:^30}'.format('ANÁLISE:'))
print(f'A soma dos valores pares é {somapar}')
print(f'A soma dos valores da 3° coluna é {soma3}')
print(f'O maior valor da 2° linha é {maior2}')
