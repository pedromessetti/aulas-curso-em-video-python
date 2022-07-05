lista = []
while True:
    n = int(input('Digite um número: '))
    if n not in lista:
        lista.append(n)
        print('Adicionado à lista!')
    else:
        print('Número repetido. Não adicionado!')
    op = str(input('Quer continuar? ')).strip().upper()[0]
    while op != 'S' and op != 'N':
        op = str(input('Digite SIM ou NÃO: ')).strip().upper()[0]
    if op == 'N':
        break
    elif op == 'S':
        continue
lista.sort()
print(f'Sua lista: {lista}')
