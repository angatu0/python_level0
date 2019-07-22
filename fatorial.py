num = int(input('Digite um número pra fatorar: '))
resultado = 1
contador = 1
while contador <= num:
    resultado *= contador
    contador += 1
print(resultado)