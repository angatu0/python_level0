# The goal is divide a bill
print("Let's go divide the bill in Brazil. Insert the values and insert '0' for finish")
sum = 0
valor = 1
while valor != 0:
    valor = float(input('Enter the value here in R$: '))
    sum = sum + valor
p = float(input('Enter the number of payers: '))
print(input('The total was R$ {}. Getting R$ {:.2f} for each person'.format(sum, (sum / p))))
