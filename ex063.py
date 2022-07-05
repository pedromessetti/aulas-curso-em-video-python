print('-'*40)
print('{:^40}'.format('SEQUÊNCIA DE FIBONACCI'))
print('-'*40)
n = int(input('Quantos termos você quer mostrar? '))
pt = 0
st = 1
print('{} -> {} -> '.format(pt, st), end='')
c = 3
while c <= n:
    tt = pt + st
    print('{} -> '.format(tt), end='')
    c += 1
    pt = st
    st = tt
print('Acabou')
