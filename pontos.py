import math
x1 = int(input('Digite o valor de "x": '))
y1 = int(input('Digite o valor de "y": '))
x2 = int(input('Digite o valor de "x2": '))
y2 = int(input('Digite o valor de "y2": '))
D = math.sqrt(((x2-x1)**2)+((y2-y1)**2))
if D >= 10:
    print('longe')
else:
    print('perto')