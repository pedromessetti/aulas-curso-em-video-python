n = 0
while True:
    n = int(input('\nDigite um número para ver sua tabuada: '))
    if n < 0:
        break
    else:
        print('='*15)
        for c in range(1, 11):
            print(f' {n} x {c} = {n*c}')
        print('='*15)
print('\nFIM DO PROGRAMA DE TABUADA')
