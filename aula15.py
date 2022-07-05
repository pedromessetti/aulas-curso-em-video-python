contagem = 1
while contagem <= 10:
    print(contagem, '-> ', end='')
    contagem += 1
print('FIM\n')

n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
#print('A soma dos números vale {}'.format(s))
print(f'A soma vale {s}')