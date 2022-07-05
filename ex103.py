def ficha(nome='desconhecido', gols=0):
    print(f'O jogador {nome} marcou {gols} gol(s) no campeonato.')


jogador = str(input('Nome do Jogador: ')).title().strip()
score = str(input('Quantos gols marcou? '))
print('-'*50)
if score.isnumeric():
    score = int(score)
else:
    score = 0
if jogador == '':
    ficha(gols=score)
else:
    ficha(jogador, gols=score)
