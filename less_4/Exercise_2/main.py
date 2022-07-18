# Представлен список чисел.
# Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию,
# оформить в виде списка. Для его формирования используйте генератор.

some_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 555]
my_list = [el for num, el in enumerate(some_list) if num != 0 and el > some_list[num-1]]
print(my_list)