'''
Создайте собственный класс-исключение, который должен проверять содержимое списка 
на отсутствие элементов типа строка и булево. Проверить работу исключения на реальном примере. 
Необходимо запрашивать у пользователя данные и заполнять список. 
Класс-исключение должен контролировать типы данных элементов списка.
'''
from os import system as cmd
class exception:
    def __init__(self, *args):
        self.result = []
        cmd('cls')

    def my_input(self):
        while True:
            try:
                val = int(input('Введите значения и нажимайте Enter: '))
                self.result.append(val)
                cmd('cls')
                print(f'Текущий список: {self.result}\n')
            except:
                cmd('cls')
                print(f"Недопустимое значение!")
                cmd = input(f'Начать с начала? y/n: ')

                if cmd.lower() == 'y':
                    cmd('cls')
                    print(try_except.my_input())
                elif cmd.lower() == 'n':
                    cmd('cls')
                    return f'Вы вышли.'
                    exit()
                else:
                    cmd('cls')
                    return f'Вы вышли'
                    exit()
try_except = exception()
print(try_except.my_input())