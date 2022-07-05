print('')
maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Digite o peso da {}° pessoa: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('\nO menor peso é {:.1f}\nO maior peso é {:.1f}'.format(menor, maior))
