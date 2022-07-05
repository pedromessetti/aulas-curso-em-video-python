from datetime import date
ano = int(input('\nAno de nascimento: '))
idade = date.today().year - ano
print('Tem {} anos em {}'. format(idade, date.today().year))
if idade >= 20:
    tempo = idade-18
    print('Passou {} anos da idade de alistamento'.format(tempo))
    print('Seu alistamento foi em {}'.format(date.today().year-tempo))
elif idade <= 16:
    tempo = 18-idade
    print('Faltam {} anos para idade de alistamento'.format(tempo))
    print('Seu alistamento será em {}'.format(date.today().year+tempo))
elif idade == 18:
    print('Está na hora de se alistar!\nEntre no site: https://alistamento.eb.mil.br/alistamento.action e realize seu alistamento.')
elif idade == 17:
    print('Falta 1 ano para idade de alistamento')
    print('Seu alistamento será ano que vem')
else:
    print('Passou 1 ano da idade de alistamento')
    print('Seu alistamento foi ano passado')