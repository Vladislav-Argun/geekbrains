'''
Реализовать класс «Дата», функция-конструктор которого должна принимать
дату в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц,
год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.


Здравствуйте. Я очень расстроен, дело в том, что я сделал домашку, 
и мне нужно на соревнования уезжать, думал что сдам, запустил bat файл, 
в котором есть уже готовые команды git pull, git push и т.д. 
Я случайно не тот запустил, и у меня всё сбросилось. 
Восстановление не возможно.
Пришлось всё делать с начала...
'''
class Data:
    def __init__(self, date):
        self.date = str(date)

    @classmethod
    def extract(cls, date):
        result = []

        for i in date.split():
            if i != '-': result.append(i) # пример [11, '-', 13, '-', '2021'] удалит '-'

        return int(result[0]), int(result[1]), int(result[2])
    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 0 <= year <= 2021:
                    return # игнор
                else:
                    return f'Неверно введён год'
            else:
                return f'Неверно введён месяц'
        else:
            return f'Неверно введён день'

    def __str__(self):
        return f'Дата: {Data.extract(self.date)}'


today = Data('11 - 1 - 2001')
print(today)
print(Data.valid(11, 11, 2022))
print(today.valid(11, 13, 2011))
print(Data.extract('11 - 11 - 2011'))
print(today.extract('11 - 11 - 2020'))
print(Data.valid(1, 11, 2000))