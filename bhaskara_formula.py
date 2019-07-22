import math
a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))
#entrar com os valores que serão usadas no cálculo da fórmula
x = (b**2)-(4*a*c)
#achar o valor para o calculo da raiz
if x < 0:
    print('Não tem raizes reais')
elif x == 0:
    raiz = math.sqrt(x)
    r1 = (-b+raiz)/(2*a)
    print('A única raiz é {}.'.format(r1))
else:
    raiz = math.sqrt(x)
    r1 = (-b+raiz)/(2*a)
    r2 = (-b-raiz)/(2*a)
    print('As raizes são: {} e {}.'.format(r1,r2))