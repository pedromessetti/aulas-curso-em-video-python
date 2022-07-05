n = c = maior = menor = soma = qntd = 0
resp = 'S'
while resp in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    qntd += 1
    if qntd == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    resp = str(input('Continua? [S/N] ')).strip().upper()[0]
media = soma/qntd
print('Digitou {} números e a média foi {}\nO maior foi {} e o menor foi {}'.format(qntd, media, maior, menor))