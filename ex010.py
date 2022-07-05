def volte():
    n = int(input('\nDigite um número inteiro positivo entre 0 e 9999: '))
    nstr = str(n)
    if '-' in nstr:
        return False
    if '.' in nstr:
        return False
    if len(nstr) == 4:
        print('Unidade: {}\nDezena: {}0\nCentena: {}00\nMilhar: {}000'.format(nstr[3:], nstr[2:3], nstr[1:2], nstr[:1]))
        return True
    if len(nstr) == 3:
        print('Unidade: {}\nDezena: {}0\nCentena: {}00'.format(nstr[2:], nstr[1:2], nstr[:1]))
        return True
    if len(nstr) == 2:
        print('Unidade: {}\nDezena: {}0'.format(nstr[1:], nstr[:1]))
        return True
    if len(nstr) == 1:
        print('Unidade: {}'.format(nstr))
        return True
    else:
        return False

validação2 = False
while not validação2:
        validação2 = volte()
