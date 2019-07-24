# The goal is check what is the more number between three numbers.
def maximo(x, y, z):
    if x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    else:
        return z