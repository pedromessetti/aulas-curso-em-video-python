n = int(input('\nDigite um número inteiro: '))
total = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[1;33m', end='')
        total += 1
    else:
        print('\033[1;31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes'.format(n, total))
if total == 2:
    print('Portanto é um número primo')
else:
    print('Portanto não é um número primo')
