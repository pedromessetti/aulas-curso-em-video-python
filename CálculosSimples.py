import math
print('\nOlá, sou um programa simples de cálculos.\nMe dê um número qualquer e vou calcular:\n-Seu antecessor\n-Seu sucessor\n-Seu dobro\n-Seu triplo\n-Sua raiz quadrada')
n = float(input('\nPara isso digite um número '))
print('\nAntecessor: {}\nSucessor: {}\nDobro: {}\nTriplo: {}\nRaiz quadrada: {:.3f}'.format(math.trunc(n-1), math.trunc(n+1), (n*2), (n*3), math.sqrt(n)))
