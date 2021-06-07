'''
б) бесконечный итератор, повторяющий элементы
некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle()
модуля itertools.
'''
from itertools import cycle

_list_ = ['afsa', 21, None, False, True]

for i in cycle(_list_):
    print(i)