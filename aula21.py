# Interactive Help
# Abra o Python Console e digite help(). Aparecerá todas as informações sobre a biblioteca, comando ou função
# q você digitar. Para sair basta digitar quit.

# DOCSTRINGS
# Cria um manual que ajuda o utilizador a entender o que a função criada faz e como utiliza-lá
# Quando digitar help(contador) vejo esse manual criado por alguem e aprendo a utilizar a função
def contador(i, f, p):
    """
    — Faz uma contagem simples e mostra na tela.
    :parameter i: início da contagem
    :parameter f: fim da contagem
    :parameter p: passo da contagem, isto é, de quanto em quanto a contagem irá pular.
    :return: sem retorno
    """
    for n in range(i, f+1, p):
        print(f'{n} ', end='')
    print('FIM')


help(contador)

# Parâmetros Opcionais


def somar(a, b, c=0):  # Defino o paramêtro c como nulo, ou seja, quando digitar somar(8, 4), o c tem valor = 0,
    s = a + b + c      # portanto, não afetará a função. Posso definir todos os parâmetros = 0 sem problemas.
    print(f'A soma vale {s}')


somar(3, 2, 5)
somar(8, 4)

# Escopo de Variáveis

