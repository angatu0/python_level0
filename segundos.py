# The goal is converter a total seconds in days, hours, minutes and seconds
Tseg = int(input('Please, entering a total seconds for converter: '))
days = Tseg // 86400
segr = Tseg % 86400
hour = segr // 3600
segr2 = segr % 3600
min = segr2 // 60
seg = segr2 % 60

print('{} days, {} hours, {} minutes e {} seconds.'.format(days, hour, min, seg))