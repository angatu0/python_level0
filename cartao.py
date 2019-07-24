mycard = int(input('Enter your credit card number: '))
cards = 1
cardOk = False
while cards != 0 and not cardOk:  # The goal is to insert several numbers and insert "0" for finish
    # Checker if the number of my credit card is between the numbers.
    cards = int(input('Enter new credit card number: '))
    if cards == mycard:
        cardOk = True
if cardOk:
    print('The your credit card in the list')
else:
    print('Not included')