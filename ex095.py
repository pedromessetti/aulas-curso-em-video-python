time = []
while True:
    jogador = {'Nome': str(input('Jogador: ')).strip().title()}
    jogador['Partidas'] = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    print('Quantidade de gols por jogo:')
    qntdgols = []
    total = 0
    for j in range(1, jogador['Partidas']+1):
        gols = int(input(f'Jogo {j} = '))
        total += gols
        qntdgols.append(gols)
    jogador['Gols'] = qntdgols
    jogador['Total de gols'] = total
    time.append(jogador.copy())
    op = str(input('Cadastrar +1 jogador? ')).strip().upper()[0]
    while op != 'S' and op != 'N':
        print('Digitação inválida!\nPor favor digite SIM ou NÃO')
        op = str(input('Cadastrar +1 jogador? ')).strip().upper()[0]
    if op == 'N':
        break
print('-'*60)
print('Cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*60)
for k, v in enumerate(time):
    print(f'{k+1:<3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
