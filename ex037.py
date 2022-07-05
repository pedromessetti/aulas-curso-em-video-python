n = int(input('\nDigite um número inteiro: '))
print('''
Bases de conversão:
[ 1 ] BINÁRIO
[ 2 ] OCTAL
[ 3 ] HEXADECIMAL
''')
option = int(input('Escolha uma opção: '))
print('')
if option == 1:
    print('O número {} convertido para BINÁRIO é igual a {}'.format(n, bin(n)[2:]))
elif option == 2:
    print('O número {} convertido para OCTAL é igual a {}'.format(n, oct(n)[2:]))
elif option == 3:
    print('O número {} convertido para HEXIDECIMAL é igual a {}'.format(n, hex(n)[2:]))
else:
    print('Opção inválida')
