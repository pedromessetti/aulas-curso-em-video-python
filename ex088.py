from random import randint
from time import sleep
jogador = int(input('\nQuantos jogos você deseja? '))
jogos = []
print('-'*6, f' SORTEANDO {jogador} JOGOS ', '-'*6)
for j in range(1, jogador+1):
    for n in range(0, 6):
        num = randint(1, 61)
        if num not in jogos:
            jogos.append(num)
        else:
            num = randint(1, 61)
            jogos.append(num)
            n += -1
    jogos.sort()
    print(f'Jogo {j}: {jogos}')
    jogos.clear()
    sleep(1.5)
print('-'*10, ' BOA SORTE ', '-'*10)
