'''
    Создать (программно) текстовый файл, записать в него программно
    набор чисел, разделенных пробелами. Программа должна
    подсчитывать сумму чисел в файле и выводить ее на экран.
'''

try:
    with open('task_5.txt', 'w+') as file:
        line = input('Введите цифры: ')
        file.writelines(line)
        num = line.split()
        print(sum(map(int, num)))
except IOError:
    print('Ошибка в файле')
except ValueError:
    print('Ошибка в синтаксисе! Можно вводить только числа!')