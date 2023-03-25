'''catoposto = float(input('Comprimento do cateto oposto: '))
catadjacente = float(input('Comprimento do cateto adjacente: '))
hipotenusa = (catoposto ** 2 + catadjacente ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))'''
from math import hypot
catoposto = float(input('Comprimento do cateto oposto: '))
catadjacente = float(input('Comprimento do cateto adjacente: '))
hipotenusa = hypot(catoposto, catadjacente)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))