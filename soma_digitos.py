# The goal is sum the digits.
valor = int(input('Enter a whole number: '))
sum = 0
while valor > 0:
   rest = valor % 10
   valor = (valor - rest) / 10
   sum += rest
print(int(sum))