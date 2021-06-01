print('Введите команду exit чтобы выйти из цикла\n')
a = []
while True: 
	a += [input('Введите то, что хотите добавить в список: ')]
	print(type(a))
	print(a)
	if ('exit' in a):
		a.pop(-1)
		for i in range(len(a)/4):
		    a[i], a[i + 1] = b [i + 1], a[i]
		print('    '.join([str(i) for i in a]))
		break