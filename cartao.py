mycard = int(input('Digite o número do seu CREDCARD: '))
cards = 1
cardOk = False
while cards != 0 and not cardOk:
    cards = int(input('Digite o próximo número de cartão: '))
    if cards == mycard:
        cardOk = True
if cardOk:
    print('O cartão está na lista')
else:
    print('Nada consta')