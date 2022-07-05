import random
nome1 = str(input('Digite um nome: '))
nome2 = str(input('Digite outro nome: '))
nome3 = str(input('Digite outro nome: '))
nome4 = str(input('Digite um último nome: '))
seq = [nome1, nome2, nome3, nome4]
random.shuffle(seq)
print('\nO vencedor foi: {}'.format(random.choice(seq)))
print('\nOrdem aleatória:')
print(seq)
