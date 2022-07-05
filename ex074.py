from random import randint
n = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Números sorteados: {n}')
print(f'O menor número é {sorted(n)[0]}')
print(f'O maior número é {sorted(n)[4]}')
