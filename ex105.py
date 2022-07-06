c = ('\033[m',          # 0-sem cor
     '\033[0;97;41m',   # 1-vermelho
     '\033[0;97;42m',   # 2-verde
     '\033[0;30;107m',  # 3-branco
     '\033[0;97;44m'    # 4-azul
     )


def ajuda(com):
    titulo(f'Acessando manual do comando \'{com}\'', 4)
    print(c[3])
    help(com)
    print(c[0], end='')


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f' {msg}')
    print('~' * tam)
    print(c[0], end='')


comando = ''
while True:
    titulo("SISTEMA DE AJUDA PYHELP", 2)
    comando = str(input("Função ou Biblioteca > "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 1)
