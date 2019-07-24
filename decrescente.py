# The goal is for know if the sequence is decreasing or increasing. If order is decreasing is right.
dec = True  # Starts being decreasing
ant = int(input('Enter first number: '))
valor = 1

while valor != 0 and dec:
    valor = int(input('Enter next number: '))
    if valor > ant:
        dec = False
    ant = valor
if dec:
    print('The order is decreasing. Congrats! :-)')
else:
    print('The order is increasing. Sorry :-(')