amarelo = '\033[1;33m'
azul = '\033[1;34m'
vermelho = '\033[1;31m'
n1 = float(input('\n{}Digite o 1° valor: '.format(amarelo)))
n2 = float(input('Digite o 2° valor: '))
menu = '''
{}   Menu:
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Digitar novos números
[ 5 ] Sair do programa'''.format(azul)
print(menu)
opção = int(input('  Selecione a opção: '))
while not opção == 5:
    if opção == 4:
        n1 = float(input('\n{}Digite o 1° valor: '.format(amarelo)))
        n2 = float(input('Digite o 2° valor: '))
        print(menu)
        opção = int(input('   Selecione a opção: '))
    elif opção == 1:
        soma = n1 + n2
        print('\n{}SOMA:   {} + {} = {}'.format(amarelo, n1, n2 , soma))
        print(menu)
        opção = int(input('  Selecione a opção: '))
    elif opção == 2:
        multi = n1 * n2
        print('\n{}MULTIPLICAÇÃO:   {} * {} = {}'.format(amarelo, n1, n2, multi))
        print(menu)
        opção = int(input('  Selecione a opção: '))
    elif opção == 3:
        if n1 > n2:
            print('\n{}MAIOR:   {}'.format(amarelo, n1))
            print(menu)
            opção = int(input('   Selecione a opção: '))
        else:
            print('\n{}MAIOR:   {}'.format(amarelo, n2))
            print(menu)
            opção = int(input('   Selecione a opção: '))
    else:
        opção = int(input('   {}Opção inválida.\n   {}Selecione uma opção válida: '.format(vermelho, azul)))