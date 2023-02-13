'''co = float(input('Comprimento do cateto aposto: '))
ca = float(input('Comprimento do catete adjacente: '))
hi = (co ** 2 + ca ** 2)  ** (1/2)
print('A hiponenusa vai medir {:.2f}'.format(hi))'''
# esse e o jeito sem usar o import math com math o codigo fica mais curto e rapido


import math
co = float(input('Comprimento do cateto oposto:'))
ca = float(input('comprimento do cateto adjacente:'))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))