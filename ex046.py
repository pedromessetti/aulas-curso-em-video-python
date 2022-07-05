from time import sleep
print('\nA queima de fogos vai começar em:')
for c in range(10, -1, -1):
    sleep(1)
    print('{:^32}'.format(c))
print('\n{:^32}'.format('FELIZ ANO NOVO!!!'))