def fatorial(n, show=False):
    """
    Calcula o fatorial de um número
    :param n: Número a ser calculado
    :param show: (opcional) Mostrar ou não o cálculo
    :return: O valor do fatorial do número
    """
    calculo = 1
    print('Fatorial = ', end='')
    for fat in range(n, 0, -1):
        calculo *= fat
        if show is True and fat > 1:
            print(f'{fat} x ', end='')
        if show is True and fat == 1:
            print('1 = ', end='')
    return calculo


print(fatorial(6, show=True))
help(fatorial)
