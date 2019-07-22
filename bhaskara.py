import math
a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))
c = int(input('Digite o valor de c: '))
x = (b**2)-(4*a*c)
if x < 0:
    print('esta equação não possui raízes reais')
elif x == 0:
    raiz = math.sqrt(x)
    r2 = (-b + raiz) / (2 * a)
    print('a raiz desta equação é {}'.format(r2))
else:
    raiz = math.sqrt(x)
    r1 = (-b - raiz) / (2 * a)
    r2 = (-b + raiz) / (2 * a)
    print('as raizes desta equação são: {:.6f} e {:.6f}.'.format(r1, r2))