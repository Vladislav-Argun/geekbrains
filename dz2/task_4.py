string = input("Введите строку: ")
word = []
num = 1
for a in range(string.count(' ') + 1): #счёт пробелов + 1
    word = string.split() # чтобы разбить строку нужно написать split()
    if len(str(word)) <= 10: #если длина строки меньше 11 то:
        print(f" {num}.) {word [a]}") # вывод значения номера и слова id которого равен a
        num += 1 # увеличение num
    else: # иначе
        print(f" {num}.) {word [a] [0:10]}") # вывод значения номера и слова id которого равен a, длина которого сократится до 10 символов
        num += 1 # увеличение num