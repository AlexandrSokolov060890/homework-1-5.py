sec = int(input('Введите время, в секундах: '))
hour = (sec // 3600)
minute = (sec // 60) - (int(hour) * 60)
second = (sec % 60)
print("%d:%d:%d" % (hour, minute, seconds))