val = float(input('\n\nDigite o valor do produto: R$'))
valdes = int(input('Digite o desconto (%): '))
des = val-(val*valdes/100)
print('\nO valor do produto com o desconto de {}% aplicado é de R${:.2f}'.format(valdes, des))
