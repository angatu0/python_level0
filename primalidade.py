n = int(input('Digite um número inteiro: '))
contador = 0
for x in range(1, n+1):
    if n % x == 0:
        contador += 1
if contador == 2:
    print('primo')
else:
    print('não primo')