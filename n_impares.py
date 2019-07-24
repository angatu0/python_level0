# The goal is print a list with amount "n" of the odd numbers.
n = int(input('Insert a whole number: '))
counter = 0
odd = 1
while counter < n:
    print(odd)
    counter += 1
    odd = odd + 2
