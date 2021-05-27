print('Введите команду exit чтобы выйти из цикла\n')
a = []
while True: 
	a += [input('Введите то, что хотите добавить в список: ')]
	print(type(a))
	print(a)
	if ('exit' in a):
		a.pop(-1)
		for i in range(len(a)):
		    a[i - 1], a[i] = a[i], a[i - 1]
		print('    '.join([str(i) for i in a]))
		break