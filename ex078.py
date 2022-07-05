valores = []
for pos in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {pos}: ')))
print('-='*20)
print(f'Você digitou os valores: {valores}')
print(f'O maior valor foi {max(valores)} na(s) posição(es): ', end='')
for pos, val in enumerate(valores):
    if val == max(valores):
        print(f'{pos}... ', end='')
print(f'\nO menor valor foi {min(valores)} na(s) posição(es): ', end='')
for pos, val in enumerate(valores):
    if val == min(valores):
        print(f'{pos}... ', end='')
