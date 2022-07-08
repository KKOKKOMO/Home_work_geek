# 2. Выполнить функцию, которая принимает несколько параметров,
# описывающих данные пользователя:
# имя,
# фамилия,
# год рождения,
# город проживания,
# email,
# телефон.
# Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.
def my_person(name, second_name, year_birth, city, email, telephone_number):
    return f'{name} {second_name}.{year_birth} - года рождения,' \
           f' проживающий в городе: {city}.' \
           f' email: {email} ' \
           f' telephone: {telephone_number}'


print(my_person(name='Stepan',
                city='Moscow',
                year_birth='2000',
                email='mm@bk.ru',
                second_name='Bakhmutov',
                telephone_number='+79999247457'))
