# Реализовать два небольших скрипта:
# итератор, генерирующий целые числа, начиная с указанного;
# итератор, повторяющий элементы некоторого списка,
# определённого заранее.
# Подсказка: используйте функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Предусмотрите условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3.
# При достижении числа 10 — завершаем цикл. Вторым пунктом необходимо предусмотреть условие,
# при котором повторение элементов списка прекратится.

from itertools import count, cycle
from random import randint

start_number = int(input('Input a number: '))
for i in count(start_number):
    if i <= randint(start_number, 150):
        print(i)
    else:
        break

print('\n')

some_list = [1, 'sveta', 1023, 'red', 'greend', 10.2]
for el in cycle(some_list):
    if el != some_list[-1]:
        print(el)
    else:
        break
