nome = str(input('Digite seu nome completo: ')).strip()
divid = nome.split()
print('Primeiro nome: {}'.format(divid[0].capitalize()))
print('Último nome: {}'.format(divid[len(divid)-1].capitalize()))
