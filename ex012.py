def frase():
    frase = str(input('\nDigite uma frase qualquer: ').strip().lower())
    a = frase.count('a')
    if a>1:
        print('A letra ´a´ nesta frase aparece {} vezes.\nPrimeiro na posição {}.\nÚltimo na posição {}.'.format(a, frase.find('a')+1, frase.rfind('a')+1))
        return True
    if a==1:
        print('A letra ´a´ nesta frase aparece 1 vez.\nNa posição {}'.format(frase.find('a')))
        return True
    if a==0:
        print('A letra ´a´ nesta frase não aparece nenhuma vez.')
        return True
frase()