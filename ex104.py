def leiaInt(txt):
    while True:
        num = input(txt)
        if num.isnumeric() == False:
            print('ERRO!')
            continue
        if num.isnumeric() == True:
            return num
        break


n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}')
