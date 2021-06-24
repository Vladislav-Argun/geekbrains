'''
Создайте собственный класс-исключение, который должен проверять содержимое списка 
на отсутствие элементов типа строка и булево. Проверить работу исключения на реальном примере. 
Необходимо запрашивать у пользователя данные и заполнять список. 
Класс-исключение должен контролировать типы данных элементов списка.
'''

from os import system as cmd
class Error:
    def __init__(self, *args):
        self.my_list = []

    def inp(self):
        while True:
            try:
                val = int(input('Введите значения и нажимайте Enter - '))
                self.my_list.append(val)
                cmd('cls')
                print(f'Текущий список - {self.my_list} \n ')
            except:
                print(f"Недопустимое значение - строка и булево")
                CMD = input(f'Попробовать еще раз? Y/N ')
                cmd('cls')
                if CMD.lower() == 'y':
                    print(try_except.inp())
                elif CMD.lower() == 'n':
                    cmd('cls')
                    return f'Выход'
                else:
                    cmd('cls')
                    return f'Выход'

try_except = Error(1)
print(try_except.inp())