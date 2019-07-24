# The goal is know the factorization the a number
num = int(input('Enter a number to factorize: '))
produce = 1
counter = 1
while counter <= num:
    produce *= counter
    counter += 1
print(produce)