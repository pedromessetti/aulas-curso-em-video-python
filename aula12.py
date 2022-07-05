nome = str(input('\nQual seu nome? '))
if nome == 'Pedro':
    print ('Que nome lindo!!!')
elif nome == 'Gustavo' or nome == 'Moacyr' or nome == 'Henrique':
    print('Que legal, já tive um professor com esse nome!')
elif nome in 'Ana Luana Juliana Vera':
    print('Que legal, Já tive uma professora com esse nome!')
else:
    print('Que nome merda')
print('Tenha um bom dia!')
