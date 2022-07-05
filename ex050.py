s = 0
print('\nO programa vai ler 6 números inteiros que você escolher e vai somar apenas aqueles que forem pares\n')
for c in range(1, 7):
    n = int(input('Digite o {}° número inteiro: '.format(c)))
    if n % 2 == 0:
        s += n
print('\nA soma dos números pares é igual a {}'.format(s))
