num = []
cont = 0
while True:
    num.append(int(input('Digite um número: ')))
    cont += 1
    op = str(input('Quer continuar? ')).strip().upper()[0]
    while op != 'S' and op != 'N':
        op = str(input('Digite SIM ou NÃO: ')).strip().upper()[0]
    if op == 'S':
        continue
    if op == 'N':
        print('-'*20)
        print(f'{cont} números digitados.')
        num.sort(reverse=True)
        print(f'Em ordem decrescente: {num}')
        if num.count(5) >= 1:
            print('O número 5 está na lista!')
        else:
            print('O número 5 NÃO está na lista!')
        break
