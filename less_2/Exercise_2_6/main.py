# Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами,
# то есть характеристиками товара: название, цена, количество, единица измерения.
# Структуру нужно сформировать программно, запросив все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Нужно собрать аналитику о товарах.
# Реализовать словарь, в котором каждый ключ — характеристика товара, например, название.
# Тогда значение — список значений-характеристик, например, список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }
# ...........................................................................................

items_struct = []
names_list = []
costs_list = []
quantity_list = []
unit_measure_list = []
analiz_dict = {
        'name': names_list,
        'cost': costs_list,
        'quantity': quantity_list,
        'units_measure': unit_measure_list
    }
count_items = 0
while True:
    controller = input('Введите "add" если хотите добавить товар, '
                       'для того чтобы закончить программу напишите "stop": ')
    if controller == 'add':
        count_items += 1
        name = input('Введите название товара: ')
        names_list.append(name)
        cost = float(input('Введите cтоимость товара: '))
        costs_list.append(cost)
        quantity = int(input('Введите количество товара: '))
        quantity_list.append(quantity)
        units_measure = input('Введите единицы измерения товара: ')
        unit_measure_list.append(units_measure)
        items_dict = {
            'name': name,
            'cost': cost,
            'quantity': quantity,
            'units_measure': units_measure
        }
        items_typle = (count_items, items_dict)
        items_struct.append(items_typle)
    elif controller == 'stop':
        break
for item in items_struct:
    print(item)
for k, v in analiz_dict.items():
    print(k, v)
