# 3. Реализовать функцию my_func(),
# которая принимает три позиционных аргумента и
# возвращает сумму наибольших двух аргументов.

def my_func(first, second, third):
    min_number = min(first, second, third)
    if min_number == first:
        result = second + third
    elif min_number == second:
        result = first + third
    else:
        result = first + second
    return result


print(my_func(5.6, 8, 0))
