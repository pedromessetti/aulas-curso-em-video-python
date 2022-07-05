n = cont = s = 0
print('\nDigite 999 para parar o programa\n')
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
    cont +=1
print(f'\nVocê digitou {cont} números e a soma entre eles foi {s}')
