def lin():  # Define uma função, uma rotina que vai ser usada mais de 1 vez no programa principal
    print('-' * 30)


# Programa principal
lin()  # Chamei a função lin()
print(f'{"Aprenda Python":^30}')
lin()


def mensagem(msg):  # Defini a função mensagem() e quando for usa-lá basta chamar e digitar em 'msg'
    print('-' * 30)  # oq quero q seja escrito entre as linhas
    print(f'{msg:^30}')
    print('-' * 30)


mensagem('ERRO NO SISTEMA')  # Chamei a função mensagem(msg) e na variável 'msg' escrevi ERRO NO SISTEMA
mensagem(str(input('Digite: ')))

a = 4
b = 5
s = a + b
print(s)

a = 8
b = 9
s = a + b
print(s)
# 2 funções parecidas só muda o valor na variável, para facilitar criamos a função soma(a, b)


def soma(a, b):
    s = a + b
    print(s)


soma(4, 5)  # Agora com uma função definida escrevo menos linhas e faço a mesma coisa
soma(8, 9)
soma(b=4, a=5)  # Posso alterar a ordem, porém tenho q explicitar isso dentro dos ()


def contador(*num):  # O * diz q a variável num vai receber x elementos
    print(num)  # Cria uma tupla com todos os elementos
    for v in num:
        print(f'{v} ', end='')
    print('\nFIM')
    tam = len(num)
    print(f'Recebi os valores {num} e são {tam} números.')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
valores = [7, 2, 5, 0, 4]  # Criei uma lista com valores aleatórios


def dobra(lst):  # Criei a função para dobrar os elementos da lista 'lst'
    pos = 0  # Indiquei a posição inicial 0
    while pos < len(lst):  # Enquanto o tamanho da lista for maior q 0
        lst[pos] *= 2  # O elemento na posição X da lista vai ser igual a ele mesmo vezes 2
        pos += 1  # Soma uma posição para avançar de elemento
    print(lst)


dobra(valores)
