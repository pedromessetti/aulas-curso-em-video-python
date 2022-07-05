print('')
soma = 0
cont = 0
maior = 0
nomemaior = str
for p in range(1,5):
    print('------ {}° Pessoa ------'.format(p))
    nome = str(input('Nome: ')).strip().title()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M/F): ')).strip().upper()
    if sexo == 'F':
        if idade < 21:
            cont += 1
    else:
        if p == 1:
            maior = idade
            nomemaior = nome
        else:
            if idade > maior:
                maior = idade
                nomemaior = nome
    soma += idade
    media = soma/4
print('')
print('A média de idade do grupo é de {:.0f} anos'.format(media))
print('O homem mais velho é o {} e sua idade é de {} anos'.format(nomemaior, maior))
print('Temos {} mulher(es) com menos de 21 anos'.format(cont))
