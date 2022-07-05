from random import randint
from time import sleep
from operator import itemgetter
print('ROLAM OS DADOS...')
sleep(1)
jogador = {'Jogador 1': randint(1, 6), 'Jogador 2': randint(1, 6),
           'Jogador 3': randint(1, 6), 'Jogador 4': randint(1, 6)}
rank = list()
for k, v in jogador.items():
    print(f'O {k} tirou {v}')
    sleep(1)
print('-'*20, '\nRanking do Jogadores')
print('-'*20)
rank = sorted(jogador.items(), key=itemgetter(1), reverse=True)
sleep(1)
for pos, v in enumerate(rank):
    print(f'{pos+1}° - {v[0]} ({v[1]})')
    sleep(1)
