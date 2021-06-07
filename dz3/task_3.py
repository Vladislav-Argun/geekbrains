"""
Задание 3
подвох, если будем перебирать то будет одно больше другого elif perv>vtor
Реализовать функцию, которая принимает три позиционных
аргумента, и возвращает сумму наибольших двух аргументов.
"""
num1 = int(input('Введите число 1:'))
num2 = int(input('Введите число 2:'))
num3 = int(input('Введите число 3:'))
def output(num1 , num2, num3):
    if num1 >= num3 and num2 >= num3: # если число 1 равно или больше числа 3 и число 2 равно или больше числа 3
        return num1 + num2
    elif num1 > num2 and num1 < num3:
        return num1 + num3
    else:
        return num2 + num3
print(output(num1 , num2, num3))