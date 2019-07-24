# The goal is simple, enter with data and print right.
Client = input('Insert the name of the client: ')
dayP = input('Insert the day of the pay: ')
monP = input('Insert the month of the pay: ')
value = input('Insert the value of the pay: ')
print('Hi, {}'.format(Client))
print('your invoice with pay date in {} of the {} whose value is R$ {}, is closed.'.format(dayP, monP, value))