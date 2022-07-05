from time import sleep


def lin():
    print('-='*20)


def contador(start, end, step):
    lin()
    if step < 0:
        step *= -1
    if step == 0:
        step = 1
    print(f'Contagem de {start} até {end} de {step} em {step}')
    sleep(2)
    if start > end:
        for n in range(start, end-1, -step):
            print(f'{n} ', end='', flush=True)
            sleep(0.5)
    else:
        for n in range(start, end+1, step):
            print(f'{n} ', end='', flush=True)
            sleep(0.5)
    print('FIM')


contador(1, 10, 1)
contador(10, 0, 2)
lin()
contador(int(input('Início: ')), int(input('Fim: ')), int(input('Passo: ')))
lin()
