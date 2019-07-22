print('Olá, como posso te ajudar?')
menu = input('Escolha o que gostaria de converter: \n [A] Fahrenheit > Celsius. \n [B] Segundos > Horas.\n Digite a opção aqui: ')

if menu == 'A':
    F = float(input('Digite a temperatura em Fahrenheit para converter em Celsius: '))
    C = (F - 32) * 5 / 9
    print('A temperatura é de {:.2f}ºC'.format(C))
elif menu == 'B':
    segt = int(input('Qual o total em segundos: '))
    h = segt // 3600
    sr = segt % 3600
    min = sr // 60
    srf = sr % 60
    if h == 0:
        print('{}min {}s'.format(min,srf))
    else:
        print('{}h {}min {}s'.format(h,min,srf))
        print('Espero ter ajudado. Até a próxima.')
else:
    print('Opção INVALIDA. \n Digite "A" ou "B".')
    while True:
        menu = input('Escolha o que gostaria de converter: \n [A] Fahrenheit > Celsius. \n [B] Segundos > Horas.\n Digite a opção aqui: ')
        if menu == 'A':
            break