def maior(*num):
    print('-'*30, '\nAnalisando os números:')
    for n in num:
        print(f' {n} ', end='')
    print(f'\nForam informados {len(num)} números')
    print(f'O maior valor foi {max(num)}')
    print('-'*30)


maior(0)
maior(1, 22, 3, 56, 9, 12, 15)
maior(int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(input('Digite um valor: ')))
