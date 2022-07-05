expressão = str(input('\nDigite uma expressão matemática: ')).strip()
if expressão.count('(') == expressão.count(')'):
    print('Expressão matemática válida!')
if expressão.count('(') != expressão.count(')'):
    print('Expressão matemática inválida!\nOBS: Falta parênteses...')
