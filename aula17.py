#PARTE 1
lanche = ['Hambúrguer', 'Suco', 'Pizza', 'Pudim']
lanche[3] = 'Sorvete' #Substitui o 4° elemento, no caso, o elemento 'Pudim' por 'Sorvete'
print(lanche)
lanche.append('Cookie') #Adiciona o elemento no final da lista
print(lanche)
lanche.insert(0, 'Cachorro Quente') #Adiciona o elemento na posição definida, no caso, na posição 0
print(lanche)
del lanche[3] #Elimina o elemento na 4° posição, no caso, a 'Pizza'
print(lanche)
lanche.pop(3) #Igual a del. É utilizado para eliminar o último elemento, basta não definir nada nos ()
print(lanche)
lanche.remove('Suco') #Não precisa indicar a posição, basta indicar o elemento
                      #OBS: Elimina o elemento na 1° posição em que ele aparece
print(lanche)
if 'Pizza' in lanche:
    lanche.remove('Pizza')
valores = list(range(4, 11)) #Criar uma lista sem precisar escrever todos os números
print(valores)
valores = [8, 2, 5, 4, 9, 3, 0]
valores.sort() #Coloca os valores em ordem alfabética ou em ordem crescente
print(valores)
valores.sort(reverse=True) #Coloca os valores em ordem inversa
print(valores)
len(valores) #Mostra a quantidade de elementos na lista
valores = [] #Cria uma lista vazia, tambem pode ser escrito dessa forma: valores = list()
valores.append(5)
valores.append(9)
valores.append(4)
for v in valores: #Mostra os valores de outra maneira
    print(f'{v}...', end=' ')
print('')
for pos, v in enumerate(valores): #Mostra os valores em suas posições
    print(f'Na posição {pos} tenho o valor {v}.')
valores = list()
for cont in range(0, 2): #Adiciona valores em uma lista com menos linhas de código
    valores.append(int(input('Digite um valor: ')))
print(valores)
a = [2, 3, 4, 7]
b = a #Quando se iguala uma lista a outra crio uma ligação entre elas, ou seja, oq altero em uma altero na outra
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
b = a[:] #Cria uma cópia da lista A e salva na lista B, não tendo ligação uma com a outra
b[2] = 4
print(f'Lista A: {a}')
print(f'Lista B: {b}')

#PARTE 2
dados = list()
dados.append('Pedro'), dados.append(25), dados.append('Maria'), dados.append(19), dados.append('João'), dados.append(32)
pessoas = list()
pessoas.append(dados[:]) #Cria uma cópia da lista 'dados' dentro de outra lista 'pessoas'
print(pessoas)
pessoas = [['Pedro', 21],['Maria', 19], ['João', 32]] #Outra forma de criar uma lista dentro de outra
print(pessoas)
print(pessoas[0][0]) #Escreve o item na posição 0 dentro da lista na posição 0, no caso 'Pedro'
print(pessoas[1]) #Escreve o item na posição 1 por completo dentro da lista 'pessoas', no caso 'Maria', 19
for p in pessoas:
    print(p) #Escreve a lista de forma tabular
    print(p[0]) #Vai escrever apenas os nomes dentro da lista 'pessoas'
for p in pessoas:
    print(f'{p[0]} tem {p[1]} anos.')
pessoas = []
dados = []
for c in range(0, 3): #Pede o nome e idade de 3 pessoas
    dados.append(str(input('Nome: '))) #Armazena o nome dentro da lista 'dados'
    dados.append(int(input('Idade: '))) #Armazena a idade dentro da lista 'dados'
    pessoas.append(dados[:]) #Armazena o nome e a idade dentro da lista 'pessoas'
    dados.clear() #Limpa a lista 'dados' sem interferir na lista 'pessoas'
print(pessoas)
maior = menor = 0
for p in pessoas:
    if p[1] >= 21: #Pega somente os que tem idade maior q 21 anos
        print(f'{p[0]} é maior de idade.') #Mostra os nomes de quem for maior de idade
        maior += 1 #Conta quantos maiores de idade são
    else:
        print(f'{p[0]} é menor de idade')
        menor += 1
print(f'São {maior} maiores de idade e {menor} menores de idade')