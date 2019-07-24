# The goal is defined coordinates and calc the distance.
import math
x1 = int(input('Entering the "x" value: '))
y1 = int(input('Entering the "y" value: '))
x2 = int(input('Entering the "x2" value: '))
y2 = int(input('Entering the "y2" value: '))
D = math.sqrt(((x2-x1)**2)+((y2-y1)**2))
if D >= 10:
    print('Far')
else:
    print('Near')