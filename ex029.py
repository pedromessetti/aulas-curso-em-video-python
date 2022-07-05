vel = int(input('\nVelocidade (Km/h): '))
multa = (vel-80)*7
if vel > 80:
    print('Multa = R${:.2f}'.format(multa))
