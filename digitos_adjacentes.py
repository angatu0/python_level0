n = int(input('Digite um número inteiro: '))
resto = n % 10
n = n // 10
x = 0
adj = False
while n > 0 and not adj:
    n3 = n % 10
    if n3 == resto:
        adj = True
    else:
        x += 1
        resto = n3
        n = n // 10
if adj:
    print('sim')
else:
    print('não')
