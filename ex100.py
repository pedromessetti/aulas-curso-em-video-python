from random import randint
from time import sleep
numeros = []
somapar = 0
for e in range(0, 5):
    n = randint(1, 10)
    numeros.append(n)
    if n in numeros:
        numeros.pop()
        n = randint(1, 10)
        numeros.append(n)
        e -= 1
numeros.sort()
print('Os números sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='', flush=True)
    sleep(0.5)
    if n % 2 == 0:
        somapar += n
print(f'\nA soma dos valores pares de {numeros} é igual a {somapar}')

