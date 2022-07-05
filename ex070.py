s = c = menor = cont = 0
nmenor = ''
while True:
    produto = str(input('\nProduto: ')).strip()
    preço = float(input('Preço: R$'))
    s += preço
    cont += 1
    if cont == 1 or preço < menor:
        menor = preço
        nmenor = produto
    if preço > 1000:
        c += 1
    op = str(input('Quer continuar? ')).strip().upper()[0]
    while op not in 'SN':
        op = str(input('Quer continuar? ')).strip().upper()[0]
    if op == 'N':
        print('\n{:-^40}'.format(' FIM DAS COMPRAS '))
        print(f'Total de R${s:.2f}'), print(f'{c} produtos custam mais de R$1000.00'), print(f'Produto mais barato foi {nmenor} custando R${menor:.2f}')
        break
