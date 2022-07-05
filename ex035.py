r1 = float(input('\n1° Reta (cm): '))
r2 = float(input('2° Reta (cm): '))
r3 = float(input('3° Reta (cm): '))
rs = [r1, r2, r3]
rs.sort()
if (rs[0]+rs[1])>rs[2]:
    if rs[0] == rs[1] == rs[2]:
        print('É possível formar um triângulo equilátero com estas retas, pois possui todos os lados de tamanhos iguais')
    elif rs[0] != rs[1] != rs[2]:
        print('É possível formar um triângulo escaleno com estas retas, pois possui todos os lados de tamanhos diferentes')
    else:
        print('É possível formar um triângulo isósceles, pois possui 2 lados iguais')
else:
    print('Não é possível formar um triângulo com estas retas')
