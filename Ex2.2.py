# This function is for entering multiple numbers and entering "0" to finish.
def main():
    n = int(input('Entering a number: '))
    sum0 = 0
    while n != 0:
        sum0 = sum0 + n
        n = int(input('Entering a number: '))
    # Once completed, print the sum result.
    print('The sum result is {}'.format(sum0))