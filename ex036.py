vermelho = '\033[1;31m'
verde = '\033[1;32m'
limpa = '\033[m'
print('\n\033[1;32;40m  BANCO MESSETTI  {}\n\nPor favor, forneça os seguintes dados para saber se seu empréstimo será:\n{}APROVADO\n{}NEGADO{}'.format(limpa,verde, vermelho, limpa))
casa = float(input('\nDigite o valor do imóvel: R$'))
salario = float(input('Digite seu salário: R$'))
anos = int(input('Quantos anos de financiamento? '))
parcelas = anos*12
valor_prestacao = casa/parcelas
print('Você terá de pagar R${:.2f} em {}x s/ juros.'.format(valor_prestacao, parcelas))
if valor_prestacao>(0.3*salario):
    print('{}EMPRÉSTIMO NEGADO{}'.format(vermelho, limpa))
else:
    print('{}EMPRÉSTIMO APROVADO{}'.format(verde, limpa))
