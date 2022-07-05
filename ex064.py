c = soma = n = 0
n = int(input('Digite um número [999 para PARAR]: '))
while n != 999:
    c += 1
    soma += n
    n = int(input('Digite um número [999 para PARAR]: '))
print('Você digitou {} números e a soma entre eles é {}'.format(c, soma))