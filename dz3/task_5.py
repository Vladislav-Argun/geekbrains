""" 
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. 
При нажатии Enter должна выводиться сумма чисел. 
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. 
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. 
Но если вместо числа вводится специальный символ, выполнение программы завершается. 
Если специальный символ введен после нескольких чисел, то 
вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого 
завершить программу.
"""
def my_func():
    print('Введите любую букву, чтобы выйти')
    _sum_ = 0
    b = False
    while b == False: 
        number = input('\nВведите числа: ').split() # в список
        result = 0
        for i in range(len(number)):
            result = result + int(number[i]) # из текста в цифру
        _sum_ = _sum_ + result
        print(f'\nОтвет: {_sum_}')
    print(f'\nИтог: {_sum_}')
my_func()