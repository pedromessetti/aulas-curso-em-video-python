import random
from time import sleep
branco = '\033[1;97m'
azul_claro = '\033[1;94m'
amarelo = '\033[1;33m'
azul = '\033[1;34m'
vermelho = '\033[1;31m'
verde = '\033[1;32m'
print('{}-='.format(azul_claro)*25)
print('{}Escolhi um número entre 0 e 10. Tente adivinhar...'.format(branco))
print('{}-='.format(azul_claro)*25)
n = random.randint(0, 10)
n2 = int(input('\n{}Qual número escolhi? '.format(azul)))
cont = 1
while n2 > 10 or n2 < 0:
    print('{}Digitação inválida. Escolha um número entre 0 e 10'.format(vermelho))
    n2 = int(input('{}Qual número escolhi? '.format(azul)))
print('{}Processando...'.format(amarelo))
sleep(3)
while n != n2:
    print('{}\nNão foi desta vez!'.format(vermelho))
    sleep(1)
    n2 = int(input('{}\nQual número escolhi? '.format(azul)))
    cont += 1
    print('{}Processando...'.format(amarelo))
    sleep(3)
print('{}\nParabéns, você acertou!\n{}O número escolhido foi {} e você acertou em {} tentativas'.format(verde, amarelo, n, cont))
