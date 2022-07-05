from datetime import date
print('\nAno atual = 0')
ano = int(input('Ano que deseja analisar: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('\nO ano {} é um ano bissexto'.format(ano))
else:
    print('\nO ano {} não é um ano bissexto'.format(ano))
