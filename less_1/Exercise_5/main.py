profit = float(input('Введите выручку фирмы: '))
costs = float(input('Введите издержки фирмы: '))
if profit > costs & costs != 0:
    print(f'Фирма работает с прибылью. Рентабельность выручки составила {profit / costs:.2f}')
    workers = int(input('Введите количество сотрудников: '))
    print(f'прибыль в расчете на одного сторудника сотавила {profit / workers:.2f}')
elif costs == 0:
    print('Вы создали что-то невероятное!!!')
elif profit == costs:
    print('Фирма работает в нуль')
else:
    print('Фирма работает в минус')

