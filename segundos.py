Tseg = int(input('Por favor, entre com o número de segundos que deseja converter: '))
dias = Tseg // 86400
segr = Tseg % 86400
hora = segr // 3600
segr2 = segr % 3600
min = segr2 // 60
seg = segr2 % 60

print('{} dias, {} horas, {} minutos e {} segundos.'.format(dias, hora, min, seg))