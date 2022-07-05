import math
angulo = int(input('\n\nDigite um ângulo qualquer (em graus): '))
gpr = math.radians(angulo)
print('Este ângulo é igual á {:.2f} radianos.'.format(gpr))
print('O valor do seno de {}° é {:.2f} radianos.'.format(angulo, math.sin(gpr)))
print('O valor do cosseno de {}° é {:.2f} radianos.'.format(angulo, math.cos(gpr)))
print('O valor da tangente de {}° é {:.2f} radianos.'.format(angulo, math.tan(gpr)))
