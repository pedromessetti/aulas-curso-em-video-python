from math import sqrt, floor, ceil
num = float(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz aproximada para o menor valor é {}'.format(floor(raiz)))
print('A raiz aproximada para o maior valor é {}'.format(ceil(raiz)))
