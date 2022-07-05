dados = dict()  # Cria um dicionário
dados = {'nome': 'Pedro', 'idade': 25}  # Cria um dicionário com a posição 'nome' e 'idade'
print(dados['nome'])  # Escreve o item na posição 'nome', no caso 'Pedro'
print(dados['idade'])  # Escreve o item na posição 'idade', no caso 25
dados['sexo'] = 'M'  # Cria uma posição 'sexo' e adiciona o item 'M' na posição 'sexo'
del dados['idade']  # Elimina a posição 'idade' e os elementos contidos nela

filme = {'título': 'Star Wars',
         'ano': 1977,
         'diretor': 'George Lucas'}
print(filme.values())  # Mostra os valores no dicionário filme, ou seja, 'Star Wars, 1977, George Lucas'
print(filme.keys())  # Mostra as posições, ou seja, 'título, ano, diretor'
print(filme.items())  # Mostra valores e posições juntos
for k, v in filme.items():  # Para as posições 'k' temos os valores 'v' no dicionário filme
    print(f'O {k} é {v}')
locadora = [filme]  # Adiciona o filme na lista 'locadora'
print(locadora[0]['ano'])  # Mostra o item na posição 0 na lista e o item na posição 'ano' no dicionário

pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
pessoas['nome'] = 'Leandro'
pessoas['peso'] = 60.5
for k in pessoas.keys():  # Mostra as posições 'k' em 'pessoas'
    print(k)
for v in pessoas.values():  # Mostra os valores 'v' em 'pessoas'
    print(v)

estado1 = {'UF': 'Rio de Janeiro', 'Sigla': 'RJ'}
estado2 = {'UF': 'São Paulo', 'Sigla': 'SP'}
brasil = [estado1, estado2]
print(brasil)

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['UF'] = str(input('Unidade Federativa: '))
    estado['Sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
print(brasil)
for e in brasil:
    for k, v in e.items():
        print(f'{k}: {v}')
    for v in e.values():
        print(v)
