# Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.


class Car:
    def __int__(self, speed, color, name, is_police=None):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_polise = is_police

    @staticmethod
    def go():
        return 'Car is runnig'

    @staticmethod
    def stop():
        return 'The car stopped'

    @staticmethod
    def turn(direction):
        return f'The car turned to the {direction}'

    def show_speed(self):
        result = self.speed
        return result


class TownCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__int__(speed, color, name, is_police)

    def show_speed(self):
        print(f'{self.speed}')
        if self.speed > 60:
            print('Attention speed limit is 60')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__int__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__int__(speed, color, name, is_police)

    def show_speed(self):
        print(f'{self.speed}')
        if self.speed > 40:
            print('Attention speed limit is 40')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__int__(speed, color, name, is_police)


audi = SportCar(100, 'Red', 'Audi')
oka = TownCar(30, 'White', 'Oka')
lada = WorkCar(70, 'Rose', 'Lada')
ford = PoliceCar(110, 'Blue',  'Ford')
print(lada.turn('left'))
print(f'When {oka.turn("right")}, then {audi.stop()}')
print(f'{lada.go()} with speed exactly {lada.show_speed()}')
print(f'{lada.name} is {lada.color}')
print(f'Is {audi.name} a police car? {audi.is_polise}')
print(f'Is {lada.name}  a police car? {lada.is_polise}')
print(audi.show_speed())
oka.show_speed()
print(ford.is_polise)
print(ford.show_speed())
