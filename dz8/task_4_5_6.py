'''
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. 
А также класс «Оргтехника», который будет базовым для классов-наследников. 
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). 
В базовом классе определить параметры, общие для приведенных типов. 
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники. 

Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники 
на склад и передачу в определенное подразделение компании. Для хранения данных 
о наименовании и количестве единиц оргтехники, а также других данных, можно использовать 
любую подходящую структуру, например словарь.

Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых 
пользователем данных. Например, для указания количества принтеров, отправленных 
на склад, нельзя использовать строковый тип данных. 
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» 
максимум возможностей, изученных на уроках по ООП.
'''
from os import system as cmd
class StoreMashines:
    cmd('cls') # чтобы избавится от старых логов
    def __init__(self, name, price, quantity, number_of_lists, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists
        self.store_all = []
        self.store = []
        self.unit = {'Модель устройства': self.name, 'Цена за еденицу': self.price, 'Количество': self.quantity}

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantity}'

    # @classmethod
    # @staticmethod
    def reception(self):
        # print(f'Для выхода - Q, продолжение - Enter')
        # while True:
        try:
            unit_name = input(f'Наименование: ')
            unit_price = int(input(f'Цена за еденицу: '))
            unit_quantity = int(input(f'Кол-во: '))
            unit_model = {'Модель устройства': unit_name, 'Цена за еденицу': unit_price, 'Количество': unit_quantity}
            self.unit.update(unit_model)
            self.store.append(self.unit)
            print(self.store)
        except:
            return 'Ошибка. Данные введены неверно.'

        print('Выход - Q\nОчистка - C\nПродолжить - Enter')
        q = input(f'CMD: ').lower()
        if q.lower() == 'c':
            self.store_all.append(self.store)
            return '\nОчистка\n'
        elif q.lower() == 'q':
            cmd('cls')
            exit()
        else:
            return StoreMashines.reception(self)


class Printer(StoreMashines):
    def to_print(self):
        return f'Time to print: {self.numb}'


class Scanner(StoreMashines):
    def to_scan(self):
        return f'Time to scan: {self.numb}'


class Copier(StoreMashines):
    def to_copier(self):
        return f'Time to copier: {self.numb}'


unit_1 = Printer('arg 1', 1, 4, 7)
unit_2 = Scanner('arg 2', 2, 5, 8)
unit_3 = Copier('arg 3', 3, 6, 9)

print(unit_1.reception())
print(unit_2.reception())
print(unit_3.reception())