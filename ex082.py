num = []
while True:
    num.append(int(input('Digite um número: ')))
    op = str(input('Quer continuar? ')).strip().upper()[0]
    while op != 'S' and op != 'N':
        op = str(input('Digite SIM ou NÃO: ')).strip().upper()[0]
    if op == 'S':
        continue
    if op == 'N':
        break
print('-'*20)
num.sort()
par = []
impar = []
for n in num:
    if n % 2 == 0:
        par.append(n)
    if n % 2 == 1:
        impar.append(n)
print(f'A lista é: {num}')
print(f'A lista dos pares é: {par}')
print(f'A lista dos ímpares é: {impar}')
