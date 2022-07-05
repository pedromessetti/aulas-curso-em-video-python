dias = int(input('Dias alugados: '))
km = float(input('Km rodados: '))
valor = (dias*60)+(km*0.15)
print('O total a pagar é R${:.2f}'.format(valor))
