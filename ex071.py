print('\nNotas disponíveis: R$50 - R$20 - R$10')
valor = int(input('Valor do saque: R$'))
nota = 50
totnota = 0
while valor % 10 != 0:
    print('\nNotas disponíveis: R$50 - R$20 - R$10')
    valor = int(input('Valor do saque: R$'))
while True:
    if valor >= nota:
        valor -= nota
        totnota += 1
    else:
        if totnota > 0:
            print(f'{totnota} notas de R${nota}')
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        totnota = 0
        if valor == 0:
            break

