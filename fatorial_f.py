# This function for know the factorial
def fatorial (n):
    f = 1
    while (n > 1):
        f *= n
        n = n - 1
    return f

# This is formula for know binomial coefficient
def f_binomial(n, k):
    return fatorial(n) / (fatorial(k)*fatorial(n-k))

# This is test for the function factorial
def testa_f ():
    if fatorial(1) == 1:
        print('funciona para 1')
    else:
        print('NÃO funciona para 1')
    if fatorial(2) == 2:
        print('funciona para 2')
    else:
        print('NÃO funciona para 2')
    if fatorial(0) == 1:
        print('funciona para 0')
    else:
        print('NÃO funciona para 0')
    if fatorial(5) == 120:
        print('funciona para 5')
    else:
        print('NÃO funciona para 5')

# This is test for the function binomial
def teste_bi():
    if f_binomial(5, 2) == 10:
        print('OK')
    if f_binomial(10, 8) == 45:
        print('OK')
    else:
        print('Errado')
