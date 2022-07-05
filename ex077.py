palavras = ('programar', 'computador', 'softwares', 'python', 'tuplas',
            'listas', 'linguagem', 'estudo', 'videoaula', 'curso')
for p in palavras:
    print(f'\nEm {p.upper()} temos as vogais: ', end='')
    for vogais in p:
        if vogais.lower() in 'aeiou':
            print(vogais, end=' ')
