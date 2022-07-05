preco = float(input('\nPreço: R$'))
dinche = preco-(0.1*preco)
cartao = preco-(0.05*preco)
juros = (0.2*preco)+preco
print('''\nFormas de pagamento:
 [ 1 ] Dinheiro   (10% de desconto)
 [ 2 ] Cheque     (10% de desconto)
 [ 3 ] Cartão:    
          À vista (5% de desconto)
           Até 2x (s/ juros)
           Até 6x (20% de juros)''')
pagamento = int(input('\nSelecione a forma de pagamento: '))
if pagamento == 3:
    parcelas = int(input('''
    1x parcela  de R${:.2f}
    2x parcelas de R${:.2f}
    3x parcelas de R${:.2f}
    4x parcelas de R${:.2f}
    5x parcelas de R${:.2f}
    6x parcelas de R${:.2f}
    
Digite a quantidade de parcelas: '''.format(cartao, preco/2, juros/3, juros/4, juros/5, juros/6)))
    if parcelas == 1:
        print('\nO valor total é R${:.2f}'.format(cartao))
    elif parcelas == 2:
        print('\nO valor total é R${:.2f}\n2x parcelas de R${:.2f}'.format(preco, preco/2))
    elif parcelas > 2 and parcelas <= 6:
        print('\nO valor total é R${:.2f}'.format(juros))
        if parcelas == 3:
            print('3x parcelas de R${:.2f}'.format(juros/3))
        elif parcelas == 4:
            print('4x parcelas de R${:.2f}'.format(juros/4))
        elif parcelas == 5:
            print('5x parcelas de R${:.2f}'.format(juros/5))
        elif parcelas == 6:
            print('6x parcelas de R${:.2f}'.format(juros/6))
    elif parcelas > 6:
        print('O limite de parcelas é 6x')
elif pagamento == 1 or pagamento == 2:
    print('O valor total é R${:.2f}'.format(dinche))
else:
    print('Deve digitar uma das 3 opções')
