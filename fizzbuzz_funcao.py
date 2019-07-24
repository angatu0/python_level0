# This function checker if the number in "x" is multiple of the 3 and 5, 3 or 5.
# If no condition is true, return the insert number.
def fizzbuzz(x):
    if (x % 3) == 0 and (x % 5) == 0:
        return 'FizzBuzz'
    elif (x % 3) == 0:
        return 'Fizz'
    elif (x % 5) == 0:
        return 'Buzz'
    else:
        return x