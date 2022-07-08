time = int(input('Введите время в секундах: '))
time_hours = time // 3600
time_minuts = (time - time_hours * 3600) // 60
time_sec = time - (time_hours * 3600 + time_minuts * 60)
print(f'{time_hours}:{time_minuts}:{time_sec}')
