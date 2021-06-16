'''
    Необходимо создать (не программно) текстовый файл, где
    каждая строка описывает учебный предмет и наличие лекционных,
    практических и лабораторных занятий по этому предмету и их
    количество. Важно, чтобы для каждого предмета не обязательно
    были все типы занятий. Сформировать словарь, содержащий
    название предмета и общее количество занятий по нему. 
    Вывести словарь на экран.
    Примеры строк файла: Информатика:
    100(л)   50(пр)   20(лаб).
    
    Физика:   30(л)   —   10(лаб)
    Физкультура:   —   30(пр)   —
    Пример словаря: {“Информатика”: 170, “Физика”: 40,
    “Физкультура”: 30}
'''
subject = {}
try:
    with open("task_6.txt", 'r', encoding='utf-8') as file:
        for line in file.readlines():
            data = line.replace('(', ' ').split()

            subject[data[0][:-1]] = sum(int(i) for i in data if i.isdigit()) # я использовал [:-1], потому что последний элемент в каждой строке - \n
except ValueError:
    print("Неконсистентные данные")
except IOError as error:
    print(error)
print(subject)