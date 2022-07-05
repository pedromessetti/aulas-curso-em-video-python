sal = float(input('\nDigite o salário do funcionário: R$'))
if sal>1250:
    novosal = ((10/100)*sal)+sal
    print('O salário com um aumento de 10% será de R${:.2f}'.format(novosal))
if sal<=1250:
    novosal = ((15/100)*sal)+sal
    print('O salário com um aumento de 15% será de R${:.2f}'.format(novosal))
