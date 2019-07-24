import math
a = int(input('Digite o valor de a: '))
#  This is the value of "a" in the quadratic equation
b = int(input('Digite o valor de b: '))
#  This is the value of "b" in the quadratic equation
c = int(input('Digite o valor de c: '))
#  This is the value of "c" in the quadratic equation

x = (b**2)-(4*a*c)
#  This is the structure for find value of the radicand of the square root

if x < 0:  # Option to find unreal roots
    print('esta equação não possui raízes reais')  # Text: "This equation has no real roots"

elif x == 0:  # Option to find one real root
    raiz = math.sqrt(x)  # This function imported from the "math" library makes it easy to find the square root
    r2 = (-b + raiz) / (2 * a)  # This is structure for find the positive square root only
    print('a raiz desta equação é {}'.format(r2))

else:
    raiz = math.sqrt(x)
    r1 = (-b - raiz) / (2 * a)
    r2 = (-b + raiz) / (2 * a)
    # Above are options both find positive and negative square roots
    # Below, use the ":.6f" was requirement the question in my course. This is optional
    print('as raizes desta equação são: {:.6f} e {:.6f}.'.format(r1, r2))