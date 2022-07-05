num = []
cont = 0
for pos in range(0, 5):
    n = int(input('Digite um número: '))
    cont += 1
    if cont == 1:
        num.append(n)
        print('Primeiro número adicionado com sucesso...')
    else:
        if n < num[0]:
            num.insert(0, n)
            print('Número adicionado na primeira posição da lista...')
        elif n > max(num):
            num.append(n)
            print('Número adicionado na última posição da lista...')
        elif n < num[1]:
            num.insert(1, n)
            print('Número adicionado na segunda posição da lista...')
        elif n < num[2]:
            num.insert(2, n)
            print('Número adicionado na terceira posição da lista...')
        elif n < num[3]:
            num.insert(3, n)
            print('Número adicionado na quarta posição da lista...')
print(f'Os números digitados em ordem crescente são: {num}')