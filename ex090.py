dic = {'nome': str(input('Nome do aluno: ')).strip().title()}
dic['media'] = float(input(f'Média de {dic["nome"]}: '))
print(f'\n{dic["nome"]} tem média igual a {dic["media"]}. Portanto sua situação é ', end='')
if 10 >= dic['media'] >= 7:
    print('Aprovado')
if 0 <= dic['media'] < 7:
    print('Reprovado')
if 0 > dic['media'] or dic['media'] > 10:
    print('''...\nNão foram cadastrados dados corretamente para definir uma situação
Reinicie o programa e tente novamente''')
