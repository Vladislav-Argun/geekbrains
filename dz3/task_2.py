"""
2. Реализовать функцию, принимающую несколько параметров, 
описывающих данные пользователя: имя, фамилия, год рождения, 
город проживания, email, телефон. Функция должна принимать параметры 
как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
"""
name = input('Введите имя: ')
last_name = input('Введите фамилию: ')
birthday = input('Введите день рождения: ')
email = input('Введите e-mail: ')
phone = int(input('Введите номер телефона: +'))
def data(name, last_name, birthday, email, phone):
	print(f"\n\nВаши данные: \nИмя: {name} \nФамилия: {last_name} \nДень рождения: {birthday} \nE-mail: {email} \nНомер телефона: +{phone}")
data(name, last_name, birthday, email, phone)