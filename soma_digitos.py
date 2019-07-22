valor = int(input('Digite um número inteiro: '))
soma = 0
while valor > 0:
   resto = valor % 10
   valor = (valor - resto)/10
   soma += resto
print(int(soma))