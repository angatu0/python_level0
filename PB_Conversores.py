# The goal is load menu with two options for choose which convert mode.
# In addition to humanize more the interaction.
print('Hi, How to help you?')
menu = input('Choose the convert mode:: \n [A] Fahrenheit > Celsius. \n [B] Seconds > Hours.\n Enter your option: ')
if menu == 'A':  # Choose temperature, ask the value.
    F = float(input('Entering the temperature in Fahrenheit for convert in Celsius: '))
    C = (F - 32) * 5 / 9
    print('The temperature is {:.2f}ºC'.format(C))
elif menu == 'B':
    segt = int(input('What is the total time in seconds: '))
    h = segt // 3600
    sr = segt % 3600
    min = sr // 60
    srf = sr % 60
    if h == 0:
        print('{}min {}s'.format(min,srf))
    else:
        print('{}h {}min {}s'.format(h,min,srf))
        print('Hope this helps. I see you later.')
else:
    while menu != 'A' and 'B':
        print('Invalid option. Entering "A" or "B".')
        menu = input('Choose what you would like to convert:'
                     '\n [A] Fahrenheit > Celsius.'
                     '\n [B] Seconds > Hours.'
                     '\n Entering thr option here: ')
        if menu == 'A':  # Choose temperature, ask the value.
            F = float(input('Entering the temperature in Fahrenheit for convert in Celsius: '))
            C = (F - 32) * 5 / 9
            print('The temperature is {:.2f}ºC'.format(C))
        elif menu == 'B':
            segt = int(input('What is the total time in seconds: '))
            h = segt // 3600
            sr = segt % 3600
            min = sr // 60
            srf = sr % 60
            if h == 0:
                print('{}min {}s'.format(min, srf))
            else:
                print('{}h {}min {}s'.format(h, min, srf))
                print('Hope this helps. I see you later.')