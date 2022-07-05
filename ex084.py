pessoas = []
dados = []
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')).strip().title())
    dados.append(float(input('Peso (kg): ')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    op = str(input('Quer continuar? ')).strip().upper()[0]
    while op != 'N' and op != 'S':
        op = str(input('Digite SIM ou NÃO: ')).strip().upper()[0]
    if op == 'S':
        continue
    if op == 'N':
        break
print('-='*20)
print(f'Cadastrou {len(pessoas)} usuários.')
print(f'O maior peso foi de {maior} Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'"{p[0]}" ', end='')
print(f'\nO menor peso foi de {menor} Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'"{p[0]}" ', end='')
