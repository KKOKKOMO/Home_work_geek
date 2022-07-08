#  Программа принимает действительное положительное число x и целое отрицательное число y.
#  Выполните возведение числа x в степень y.
#  Задание реализуйте в виде функции my_func(x, y).
#  При решении задания нужно обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами.
#  Первый — возведение в степень с помощью оператора **.
#  Второй — более сложная реализация без оператора **,
#  предусматривающая использование цикла.
# float x > 0, int y < 0
def my_func(x, y):
    result = 1
    for _ in range(abs(y)):
        result *= x
    result = 1 / result
    return result


def my_func_2(x, y):
    return x ** y


while True:
    f_number = float(input('Input a float number in range (0:inf): '))
    s_number = int(input('Input a int number in range (-inf:0): '))
    if f_number > 0 > s_number:
        print(my_func(f_number, s_number))
        print(my_func_2(f_number, s_number))
        break
    else:
        print('Some number is incorrectly')
        continue
