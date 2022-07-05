frase = str(input('\nDigite uma frase qualquer: ')).strip().upper().split()
junta = ''.join(frase)
invertida = ''.join(reversed(junta))
print('\nO inverso de {} é {}'.format(junta, invertida))
if junta == invertida:
    print('Temos um palíndromo')
else:
    print('Não é um palíndromo')
