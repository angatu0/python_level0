# The goal is know if there are adjacent numbers
n = int(input('Insert whole number: '))
rest = n % 10
n = n // 10
x = 0
adj = False
while n > 0 and not adj:
    n2 = n % 10
    if n2 == rest:
        adj = True
    else:
        x += 1
        rest = n2
        n = n // 10
if adj:
    print('Yes')
else:
    print('No')
