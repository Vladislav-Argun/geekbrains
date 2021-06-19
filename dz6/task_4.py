'''
Реализуйте базовый класс Car. У данного класса должны быть
следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны
сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar,
PoliceCar. Добавьте в базовый класс метод show_speed, который
должен показывать текущую скорость автомобиля. Для классов TownCar
и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
'''
class Car:
    # atributes
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    # methods
    def go(self):
        return f'\n{self.name} is started'

    def stop(self):
        return f'\n{self.name} is stopped'

    def turn_right(self):
        return f'\n{self.name} is turned right'

    def turn_left(self):
        return f'\n{self.name} is turned left'

    def show_speed(self):
        return f'\nCurrent speed {self.name} is {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of town car !!! {self.name} is {self.speed}')

        if self.speed > 40:
            return f'\nSpeed: {self.name} is higher than allow for town car !!!'
        else:
            return f'\nSpeed: {self.name} is normal for town car !!!'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of work car !!! {self.name} is {self.speed}')

        if self.speed > 60:
            return f'\nSpeed: {self.name} is higher than allow for work car !!!'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police == True:
            return f'\n{self.name} is from LSPD'
        else:
            return f'\n{self.name} is not from LSPD'

# settings and args
ford = PoliceCar(90, 'Yellow', 'Ford', True)
bmw = WorkCar(120, 'Green', 'BMW X5', False)
zhiguli = TownCar(60, 'Black', 'Zhiguli', False)
kia = TownCar(80, 'White', 'Kia Sorento', False)

# actions
print(bmw.turn_left())
print(f'{bmw.go()} with speed exactly {bmw.show_speed()}')
print(f'{zhiguli.turn_right()} and {ford.stop()}')

# is a police car?
print(f'{ford.name} - police car? {ford.is_police}')
print(f'{bmw.name} - police car? {bmw.is_police}')

# color
print(f'{bmw.name} color is {bmw.color}')

# show speed and speed status
print(ford.show_speed())
print(zhiguli.show_speed())
print(kia.show_speed())