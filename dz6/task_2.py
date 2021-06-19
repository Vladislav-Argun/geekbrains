'''
Реализовать класс Road (дорога), в котором определить атрибуты:
length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании
экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого
для покрытия всего дорожного полотна.
Использовать формулу: длина*ширина*масса асфальта
для покрытия одного кв метра дороги асфальтом, толщиной
в 1 см*число см толщины полотна. Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т
'''
class Road:
    def __init__(self, _length, _width, _m):
        self._length = int(_length)
        self._width = int(_width)
        self._m = int(_m)

    def get_asphalt_weight(self):
        return self._length * self._width * self._m


my_road = Road(10, 5, 2)
print(my_road.get_asphalt_weight())
# я бы сделал так:
# def count(width, heigth, m):
#     result = int(width) * int(heigth) * int(m)
#     print(result)
#     return result
# width = input('Введите число ширину: ')
# heigth = input('Введите число высоту: ')
# m = input('Введите массу (авто в кг): ')
# count(width, heigth, m)