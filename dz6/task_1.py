"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск). 
Атрибут реализовать как приватный. 
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый. 
Продолжительность первого состояния (красный) составляет 7 секунд, 
второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. 
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый). 
Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""
import os
from time import sleep
from termcolor import colored
from colorama import Back, init
class TrafficLight:
	__color = ['red', 'yellow', 'green']
	i = 0
	def running(self):
		while self.i < 3: 
			init()
			os.system('color 0f')
			print(colored('	   ___\n	  /***\\\n	 /*****\\\n         |*****|\n	 \\*****/\n	  \\***/\n	   ‾‾‾\n', f'{TrafficLight.__color[self.i]}'))
			if self.i == 0:
				sleep(7)
			elif self.i == 1:
				sleep(2)
			elif self.i == 2:
				sleep(5)
			self.i += 1
TrafficLight = TrafficLight()
TrafficLight.running()

# надеюсь вам понравилось)

# Вариант решения (без переменных)
# class TrafficLight:
# 	def running():
# 		while True:
# 			os.system('cls')
# 			init()
# 			print(Back.RED + '		\n		\n		\n		')
# 			sleep(7)
# 			print(Back.YELLOW + '		\n		\n		\n		')
# 			sleep(2)
# 			os.system('color 0f')
# 			os.system('cls')
# 			print(Back.GREEN + '\n\n\n\n\n\n\n\n		\n		\n		\n		\n')
# 			sleep(5)
# 			os.system('color 0f')
# TrafficLight.running()