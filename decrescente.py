dec = True
ant = int(input('Digite o primeiro número: '))
valor = 1
while valor != 0 and dec:
    valor = int(input('Digite o próximo número: '))
    if valor > ant:
        dec = False
    ant = valor
if dec:
    print('A ordem é decrescente. Parabéns!!')
else:
    print('A ordem é crescente. Uma pena :-(')