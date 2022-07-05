from datetime import date
print('')
contmaior = 0
contmenor = 0
for c in range(1, 8):
    ano = int(input('Digite o ano de nascimento da {}° pessoa: '.format(c)))
    idade = date.today().year - ano
    if idade < 18:
        contmenor += 1
    else:
        contmaior += 1
print('{} pessoas são maiores de idade'.format(contmaior))
print('{} pessoas ainda não completaram a maior idade'.format(contmenor))
