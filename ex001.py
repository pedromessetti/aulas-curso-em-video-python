print('\n')
n = input('Digite qualquer coisa: ')
print('\n')
print('O tipo primitivo de', n,'é', type(n))
print('\n')
print(n, 'é uma palavra?', n.isalpha())
print(n, 'é um número?', n.isnumeric())
print(n, 'é alfanumérico?', n.isalnum())
print(n, 'só tem letras maiúsculas?', n.isupper())
print(n, 'só tem letras minúsculas?', n.islower())
print(n, 'começa com letra maiúsculas?', n.istitle())


