print('='*50)
print('{:^50}'.format('10 TERMOS DE UMA PROGRESSÃO ARITMÉTICA'))
print('='*50)
pt = int(input('Primeiro Termo: '))
r = int(input('Razão: '))
termo = pt
c = 1
total = 0
op = 10
while op != 0:
    total+= op
    while c <= total:
        print('{} -> '.format(termo), end='')
        termo += r
        c += 1
    print('Pausa')
    op = int(input('Digite quantos termos você quer mostrar mais: '))
print('Progressão finalizada com {} termos mostrados'.format(total))