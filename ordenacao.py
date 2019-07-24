# The goal is check the three numbers entered are in order increasing or decreasing.
n1 = int(input('Entering first whole number:'))
n2 = int(input('Entering second whole number:'))
n3 = int(input('Entering third whole number:'))
if (n1 < n2 < n3) == True:
    print('increasing')
else:
    print('This not is order increasing')