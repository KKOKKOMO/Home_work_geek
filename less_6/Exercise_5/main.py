# 5. Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw.
# Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    @staticmethod
    def draw():
        return 'Start draw'


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    @staticmethod
    def draw():
        return 'Start draw with a pen'


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    @staticmethod
    def draw():
        return 'Start draw with a pencil'


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    @staticmethod
    def draw():
        return 'Start draw with a handle'


my_huiny = Stationery('Knife')
my_pen = Pen('pen')
my_pencil = Pencil('pencil')
my_handler = Handle('handler')

print(f'{my_pen.draw()}\n{my_huiny.draw()}\n{my_pencil.draw()}\n{my_handler.draw()}')


