def lin(txt):
    print('-'*30)
    print(f'{txt:^30}')
    print('-'*30)


def area(l, c):
    a = l * c
    lin('Resultado')
    print(f'A área do terreno de {l}m por {c}m é de {a}m²')


lin('Cálculo da Área')
area(int(input('Largura (m): ')), int(input('Comprimento (m): ')))
