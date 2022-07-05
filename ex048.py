soma = 0
contador = 0
for c in range(1, 501, 2):
        if c % 3 == 0:
            contador += 1
            soma += c
print('\nA soma dos números ímpares, multiplos de 3, dentro do intervalo de 1 até 500 é {} e foram somados {} números'. format(soma, contador))
