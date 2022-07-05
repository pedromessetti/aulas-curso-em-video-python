dist = float(input('\nDistância (Km): '))
v1 = 0.5*dist
v2 = 0.45*dist
if dist<=200:
    print('Valor: R${:.2f}'.format(v1))
if dist>200:
    print('Valor: R${:.2f}'.format(v2))