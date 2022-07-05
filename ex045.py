import random
from time import sleep
limpa = '\033[m'
branca_fundo_verde = '\033[1;30;42m'
preta_fundo_branco = '\033[1;30;107m'
azul = '\033[1;34m'
vermelho = '\033[1;31m'
verde = '\033[1;32m'
cinza = '\033[1;90m'
print('{:45}'.format(branca_fundo_verde), '{}'.format(limpa))
print('\33[1;30;42m' '='*5, 'PEDRA, PAPEL OU TESOURA', '='*5, '{}' .format(limpa))
print('{:45}'.format(branca_fundo_verde), '{}'.format(limpa))
pc = random.sample([1, 2, 3], k=1)
jogador = int(input('''
[1] PEDRA
[2] PAPEL
[3] TESOURA

{}Escolha uma opção:{} '''.format(verde, limpa)))
if jogador > 3 or jogador < 1:
    print('{}JOGADA INVÁLIDA{}'.format(vermelho, limpa))
else:
    print('{}PEDRA'.format(azul))
    sleep(0.5)
    print('PAPEL')
    sleep(0.5)
    print('TESOURA{}'.format(limpa))
    sleep(0.5)
    if pc == [1] and jogador == 3 or pc == [2] and jogador == 1 or pc == [3] and jogador == 2:
        print('\n{}PERDEU!'.format(vermelho))
        if pc == [1]:
            print('Minha PEDRA amassou sua TESOURA, chora arrombado')
        if pc == [2]:
            print('Meu PAPEL enrolou sua PEDRA e atirou na casa do caralho')
        if pc == [3]:
            print('Minha TESOURA rasgou seu PAPEL otário, se fudeu')
    elif jogador == 1 and pc == [3] or jogador == 2 and pc == [1] or jogador == 3 and pc == [2]:
        print('\n{}GANHOU!'.format(verde))
        if jogador == 1:
            print('Sua PEDRA amassou minha TESOURA, toma no cu')
        if jogador == 2:
            print('Seu PAPEL enrolou minha PEDRA, me fudi')
        if jogador == 3:
            print('Sua TESOURA rasgou meu PAPEL, puta que pariu ein')
    else:
        print('\n{}EMPATOU{}'.format(cinza, limpa))