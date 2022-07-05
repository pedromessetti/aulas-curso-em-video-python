total = []
for n in range(1, 8):
    total.append(int(input(f'Digite o {n}° número: ')))
total.sort()
print('-'*20)
print('Os números pares digitados são: ', end='')
for n in total:
    if n % 2 == 0:
        print(f'{n}  ', end='')
print('\nOs números ímpares digitados são: ', end='')
for n in total:
    if n % 2 == 1:
        print(f'{n}  ', end='')
