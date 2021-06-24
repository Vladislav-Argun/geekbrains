'''
Реализовать класс «Дата», функция-конструктор которого должна принимать
дату в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц,
год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
'''
from datetime import date
class Data:
    def __init__(self, date):
        self.date = date

    @classmethod
    def get_date(cls, date):
        result = []

        for i in date.split():
            if i != '-':
                result.append(i)

        return int(result[0]), int(result[1]), int(result[2])
    @staticmethod
    def valid(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 0 <= year <= 2021:
                    return
                else:
                    return 'Неверно введён год.'
            else:
                return 'Неверно введён месяц.'
        else:
            return 'Неверно введён день.'
    def __str__(self):
        return f'Дата: {Data.get_date(self.date)}'

# class Data:
#     def __init__(self, date):
#         # self.day = day
#         # self.month = month
#         # self.year = year
#         self.date = str(date)

#     @classmethod
#     def get_date(cls, date):
#         result = []

#         for i in date.split():
#             if i != '-': result.append(i) # пример [11, '-', 12, '-', 2020] '-' не будут добавляться в result

#         return int(result[0]), int(result[1]), int(result[2])

#     @staticmethod
#     def valid(day, month, year):
#         if 1 <= day <= 31:
#             if 1 <= month <= 12:
#                 if 2019 >= year >= 0:
#                     return # игнор
#                 else:
#                     return f'Неверно введён год'
#             else:
#                 return f'Неверно введён месяц'
#         else:
#             return f'Неверно введён день'

#     def __str__(self):
#         return f'Текущая дата {Data.get_date(self.date)}'


today = Data('17 - 10 - 2007')
print(today)
print(Data.valid(7, 12, 2020))
print(today.valid(16, 6, 2009))
print(Data.get_date('28 - 11 - 2010'))
print(today.get_date('14 - 9 - 2020'))
print(Data.valid(1, 11, 2012))