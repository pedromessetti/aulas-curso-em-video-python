from datetime import date
dados = {'Nome': str(input('Nome: ')).strip().title(),
         'Idade': date.today().year - int(input('Ano de Nascimento: ')),
         'CTPS': int(input('Carteira de Trabalho (0 se não tiver): '))}
if dados['CTPS'] != 0:
    dados['Contratação'] = int(input('Ano de Contratação: '))
    dados['Aposentadoria'] = ((dados['Contratação'] + 35) - date.today().year) + dados['Idade']
print('-'*30)
for k, v in dados.items():
    print(f'{k} = {v}')
