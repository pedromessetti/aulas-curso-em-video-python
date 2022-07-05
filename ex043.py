nome = str(input('\n Olá novo usuário!\n Por favor responda as perguntas a seguir:\n   - Qual é o seu nome?  ')).strip()
peso = float(input ('   - Qual é o seu peso (kg) ? '))
altura = float(input ('   - Qual é a sua altura (m) ? '))
imc = peso/(altura**2)
print ('\n Perfeito',nome,'! Muito obrigado por fazer seu registro!')
print ('\n Seu Índice de Massa Corporal é de {:.2f}'.format(imc))
if imc <= 16:
	print("\n Isso significa que você se encontra num estado de Magreza grave\n Recomendamos que não perca tempo e procure já um médico!")
elif imc <= 17:
	print("\n Isso significa que você se encontra num estado de Magreza moderada\n Recomendamos o auxílio de um médico")
elif imc <= 18.5:
	print("\n Isso significa que você se encontra num estado de Magreza leve\n Precisa ganhar um pouco de massa para chegar no estado ideal, nada muito grave.")
elif imc <= 25:
	print("\n Isso significa que você se encontra num estado Saudável\n Parabéns!")
elif imc <= 30:
	print("\n Isso significa que você se encontra num estado de Sobrepeso\n Precisa perder um pouco de massa para chegar no estado ideal, nada muito grave.")
elif imc <= 35:
	print("\n Isso significa que você se encontra num estado de Obesidade de Grau I\n Não deixe que o problema se agrave.")
elif imc <= 40:
	print("\n Isso significa que você se encontra num estado de Obesidade de Grau II\n Uma obesidade severa, recomendamos o auxílio de um médico.")
else:
	print("\n Isso significa que você se encontra num estado de Obesidade de Grau III\n Uma obesidade mórbida, recomendamos que não perca tempo e procure já um médico!")
