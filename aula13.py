for c in range(1, 6): # O último número é desconsiderado, ou seja, a contagem vai de 1 a 5
    print('Oi')
print('Fim\n')

for c in range(0,6): # Vai contar de 0 até 5
    print(c)
print('Fim\n')

for c in range(6, 0, -1): # Para contar para trás deve sempre colocar o -1 no final
    print(c)
print('Fim\n')

for c in range(0,7,2): # Contou de 0 até 7 pulando 2 casas
    print(c)
print('Fim\n')

n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)
print('Fim\n')

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('Fim\n')

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n # Mesma coisa que s = s + n
print('A soma dos valores foi {}'.format(s))
