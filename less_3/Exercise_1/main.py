# 1. Реализовать функцию,
# принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль.
def my_division(number_1, number_2):
    result = None
    try:
        result = float(number_1) / float(number_2)
    except ZeroDivisionError:
        print('Division by zero!')
    except ValueError:
        print('You can`t input str!')
    return result


my_fisrt_number = input('Input first num: ')
my_second_number = input('Input sec num: ')
print(my_division(my_fisrt_number, my_second_number))
