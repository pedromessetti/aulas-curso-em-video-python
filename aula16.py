lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[1]), print(lanche[3]), print(lanche[-2]), print(lanche[1:3]), print(lanche[2:]), print(lanche[:2]), print(lanche[-3:])
print(lanche)

print(''), print(len(lanche)), print('')

#Tuplas são imutáveis, exemplo:
#lanche[1] = refrigerante

for comida in lanche:
    print(f'Comi {comida}')
print('Comi pra caralho!\n')

for cont in range(0, len(lanche)):
    print(lanche[cont]), print(cont)

print('')

for pos, comida in enumerate(lanche):
    print(comida), print(pos)

print(''), print(sorted(lanche))

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(''), print(c), print(len(c)), print(c.count(5)), print(c.index(5)), print(c.index(5, 2)), print('')
del c