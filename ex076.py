itens = ('Tabaco Malboro', 8, 'Smoking Slim', 0.6, 'Smoking Brown', 1, 'Filtro', 0.8, 'Piteira Raw', 0.6, 'Tesoura', 1, 'Isqueiro Clipper', 1)
print('-'*40)
for i in range(0, len(itens), 2):
    print(f'{itens[i]:.<30} {itens[i+1]:>6.2f}€')
print('-'*40)
