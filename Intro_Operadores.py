# The goal is convert degrees Fahrenheit in Celsius.
F = float(input('Insert the temperature in Fahrenheit for convert in Celsius: '))
C = (F - 32) * 5 / 9
# Detail below ":.2f" for insert two decimal places
print('The temperature is {:.2f}ºC'.format(C))
