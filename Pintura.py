l = float(input('\n\nQual é a largura em metros? '))
a = float(input('Qual é a altura em metros? '))
ar = l*a
print('\nA área que deseja pintar é de {:.3f}m²'.format(ar))
t = float(input('Agora, observe na lata e informe quantos m² a tinta pinta por L: '))
lt = ar/t
print('\nNesse caso, precisaria de {:.0f}L dessa tinta para a pintura que deseja.'.format(lt))
