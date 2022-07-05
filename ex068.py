from random import randint
from time import sleep
branco = '\033[1;97m'
azul_c = '\033[1;94m'
cinza_c = '\033[1;37m'
verm = '\033[1;31m'
cian_c = '\033[1;36m'
verde = '\033[1;32m'
print('',f'{azul_c}=' * 20, '\n{}{:^22}\n'.format(branco, 'PAR OU ÍMPAR'), f'{azul_c}=' * 20)
c = 1
while True:
    print(''), print(f'{azul_c}-'*20)
    play = str(input(f'{branco}Par ou Ímpar? ')).strip().upper()[0]
    player = int(input('Seu número: '))
    pc = randint(0, 10)
    s = pc + player
    print(f'{azul_c}-'*20)
    if 'P' in play:
        sleep(1), print(f'{branco}Você jogou {cian_c}{player}{branco} e escolheu {cian_c}PAR'), sleep(1), print(f'{branco}O computador {cinza_c}{pc}{branco} e escolheu {cinza_c}ÍMPAR.')
        if s % 2 == 0:
            sleep(0.5), print(f'{cian_c}{player} {branco}+ {cinza_c}{pc}', end=''), sleep(0.5), print(f' {branco}= {cian_c}{s}')
            print('Deu PAR...'), sleep(0.5), print(f'{verde}PARABÉNS, VOCÊ VENCEU!')
            if c == 1:
                print(f'{branco}Total de 1 tentativa.')
            else:
                print(f'{branco}Total de {c} tentativas.')
            break
        else:
            sleep(0.5), print(f'{cian_c}{player} {branco}+ {cinza_c}{pc}', end=''), sleep(0.5), print(f' {branco}= {cinza_c}{s}')
            print('Deu ÍMPAR...'), sleep(0.5), print(f'{verm}Não foi desta vez. Continue tentando!'), sleep(1)
            c +=1
    elif 'I' in play or 'Í' in play:
        sleep(1), print(f'{branco}Você jogou {cian_c}{player}{branco} e escolheu {cian_c}ÍMPAR'), sleep(1), print(f'{branco}O computador {cinza_c}{pc}{branco} e escolheu {cinza_c}PAR.')
        if s % 2 == 0:
            sleep(0.5), print(f'{cian_c}{player}{branco} + {cinza_c}{pc}', end=''), sleep(0.5), print(f'{branco} = {cinza_c}{s}')
            print('Deu PAR...'), sleep(0.5), print(f'{verm}Não foi desta vez. Continue tentando!'), sleep(1)
            c += 1
        else:
            sleep(0.5), print(f'{cian_c}{player}{branco} + {cinza_c}{pc}', end=''), sleep(0.5), print(f'{branco} = {cian_c}{s}')
            print('Deu ÍMPAR...'), sleep(0.5), print(f'{verde}PARABÉNS, VOCÊ VENCEU!')
            if c == 1:
                print(f'{branco}Total de 1 tentativa.')
            else:
                print(f'{branco}Total de {c} tentativas.')
            break
