print('\n')
n = input('Digite uma palavra e/ou um número: ')
print('\n')
if n.isalpha():
    print('É uma palavra!')
    if n.istitle():
        print('Começa com uma letra maiúscula.')
    if n.islower():
        print('Só possui letras minúsculas.')
    if n.isupper():
        print('Só possui letras maiúsculas')
if n.isnumeric():
    print('É um número!')
if n.isalnum():
    print('É alfanumérico, ou seja, tem letras e/ou números!')

print('O tipo primitivo é:', type(n))

