import math
print('\nDado um triângulo retângulo:')
co = float(input('Digite o compromimento do seu cateto oposto: '))
ca = float(input('Digite o comprimento do seu cateto adjacente: '))
print('\nA hipotenusa é igual a {}'.format(math.hypot(co,ca)))
