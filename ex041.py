limpa = '\033[m'
cat = '\033[1;36m'
print(('\033[1;46m CONFEDERAÇÃO NACIONAL DE NATAÇÃO {}').format(limpa))
from datetime import date
ano = int(input('Ano de nascimento: '))
idade = date.today().year - ano
if idade <= 9:
    print('{}CATEGORIA MIRIM{}'.format(cat, limpa))
elif idade <= 14:
    print('{}CATEGORIA INFANTIL{}'.format(cat, limpa))
elif idade <= 19:
    print('{}CATEGORIA JUNIOR{}'.format(cat, limpa))
elif idade <= 25:
    print('{}CATEGORIA SÊNIOR{}'.format(cat, limpa))
else:
    print('{}CATEGORIA MASTER{}'.format(cat, limpa))
