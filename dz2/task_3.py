# первый вариант
a = ['зима', 'весна', 'лето', "осень"]
b = int(input("Введите номер месяца: "))
if b > 0 & b <= 12:
	print(a [(b % 12) // 4] )
else:
    print("Такого месяца не существует!")
# второй
s_1 = ['зима', 'весна', 'лето', "осень"]
s_2 = {1 : 'зима', 2 : 'весна', 3 : 'лето', 4 : 'осень'}
month = int(input("Введите номер месяца: "))
if month == 1 or month == 12 or month == 2:
    print(s_2.get(1))
    print(s_1[0])
elif month == 3 or month == 4 or month == 5:
    print(s_2.get(2))
    print(s_1[1])
elif month == 6 or month == 7 or month == 8:
    print(s_2.get(3))
    print(s_1[2])

elif month == 9 or month == 10 or month == 11:
    print(s_2.get(4))
    print(s_1[3])
else:
    print("Такого месяца не существует!")