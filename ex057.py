limpa = '\033[0m'
vermelho = '\033[0;31m'
azul = '\033[1;94m'
roxo = '\033[1;95m'
amarelo = '\033[1;33m'
s = input('\n{}Informe o sexo: '.format(amarelo)).upper().strip()
while s not in 'MASCULINOFEMININO':
    s = input('{}Opção inválida. {}Por favor informe o sexo: '.format(vermelho, amarelo)).upper().strip()
if s in 'MASCULINO':
    print('Sexo salvo como {}MASCULINO'.format(azul))
if s in 'FEMININO':
    print('Sexo salvo como {}FEMININO'.format(roxo))
