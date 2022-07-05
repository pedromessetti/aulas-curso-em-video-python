tot_maior = tot_masc = tot_fem = 0
while True:
    print('-' * 20), print('{:^20}'.format('CADASTRO')), print('-' * 20)
    idade = int(input('Idade: '))
    while idade < 0:
        idade = int(input('Idade: '))
    if idade >= 18:
        tot_maior += 1
    sexo = str(input('Sexo: ')).strip().upper()[0]
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Sexo: ')).strip().upper()[0]
    if sexo == 'M':
        tot_masc += 1
    if sexo == 'F' and idade < 20:
        tot_fem += 1
    op = str(input('Registrado com sucesso!\nQuer continuar? ')).strip().upper()[0]
    while op != 'N' and op != 'S':
        op = str(input('Quer continuar? ')).strip().upper()[0]
    if op == 'N':
        print('-'*20), print('{:^20}'.format('FIM DO PROGRAMA')), print('-'*20)
        print(f'Total de {tot_maior} pessoa(s) maiores de idade.'), print(f'Total de {tot_masc} homem(s) cadastrados.'), print(f'Total de {tot_fem} mulher(es) com menos de 20 anos.')
        break
    else:
        continue
