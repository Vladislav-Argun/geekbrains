'''
Представлен список чисел. Необходимо вывести элементы
исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить
в виде списка. Для формирования списка использовать генератор.
'''
n_list = [1, 2, 4, 3, 6, 5] # n сокр. number
result = [i for num, i in enumerate(n_list) if n_list[num] > n_list[num - 1]]
print(f'До: {n_list}')
print(f'После: {result}')