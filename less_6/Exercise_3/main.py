# Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и
# дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров.

class Worker:

    def __int__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {
            "wage": wage,
            "bonus": bonus
        }


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__int__(name, surname, position, wage, bonus)

    def get_full_name(self):
        result = f'{self.name} {self.surname}'
        return result

    def get_total_income(self):
        result = f'{self._income.get("wage") + self._income.get("bonus")}'
        return result


my_person = Position('Stepan', 'Bakhmutov', 'Programmer', 100000, 80000)
print(my_person.get_full_name())
print(my_person.get_total_income())





