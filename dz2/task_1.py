print('Введите команду exit чтобы выйти из цикла\n')
result = []
while True: 
	result += [input('Введите то, что хотите добавить в список: ')]
	print(type(result))
	print(result)
	if ('exit' in result):
		result.pop(-1)
		break