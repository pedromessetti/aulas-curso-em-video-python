dados = list()
mulheres = []
pessoas = dict()
totpessoas = sidade = 0
while True:
    pessoas['Nome'] = str(input('Nome: ')).strip().title()
    totpessoas += 1
    pessoas['Idade'] = int(input('Idade: '))
    sidade += pessoas['Idade']
    pessoas['Sexo'] = str(input('Sexo: ')).strip().upper()[0]
    while pessoas['Sexo'] != 'M' and pessoas['Sexo'] != 'F':
        print('Digitação inválida!\nPor favor digite MASCULINO ou FEMININO...')
        pessoas['Sexo'] = str(input('Sexo: ')).strip().upper()[0]
    dados.append(pessoas.copy())
    if pessoas['Sexo'] == 'F':
        mulheres.append(pessoas['Nome'])
    op = str(input('Salvar +1 pessoa? ')).strip().upper()[0]
    while op != 'S' and op != 'N':
        print('Digitação inválida!\nPor favor digite SIM ou NÃO...')
        op = str(input('Salvar +1 pessoa? ')).strip().upper()[0]
    if op == 'N':
        break
    print('-'*30)
print('-'*30, f'\nTotal de {totpessoas} pessoas cadastradas')
print(f'As mulheres cadastradas foram: ', end='')
for m in mulheres:
    print(f'| {m} |', end='')
sidade /= totpessoas
print(f'\nA média de idade é {sidade:.0f} anos')
print('As pessoas cadastradas com idade acima da média foram: ', end='')
for i in dados:
    if i['Idade'] > sidade:
        print(f'| {i["Nome"]} |', end='')
print()
print('-'*6, ' FIM DO PROGRAMA ', '-'*6)
