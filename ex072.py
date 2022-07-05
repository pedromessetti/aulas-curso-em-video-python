n = ('ZERO', 'UM', 'DOIS', 'TRÊS', 'QUATRO', 'CINCO', 'SEIS', 'SETE', 'OITO', 'NOVE', 'DEZ', 'ONZE', 'DOZE', 'TREZE', 'QUATORZE', 'QUINZE', 'DEZESSEIS', 'DEZESSETE', 'DEZOITO', 'DEZENOVE', 'VINTE')
user = int(input('Digite um número entre 0 e 20: '))
while user > 20 or user < 0:
    user = int(input('Digite um número entre 0 e 20: '))
print(f'Você digitou o número {n[user]}')
