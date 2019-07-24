n = int(input('Entering the whole number: '))
counter = 0
for x in range(1, n+1):
    if n % x == 0:
        counter += 1
if counter == 2:
    print('prime number')
else:
    print('Not prime number')