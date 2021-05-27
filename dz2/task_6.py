tovars = [] 
num = 0
c = None
d = None
a = {'имя': '', 'цена': '', 'количество': '', 'eд': ''}
b = {'имя': [], 'цена': [], 'количество': [], 'eд': []}
while True:
    d = input("Для выхода введите «exit».\nДля изменения введите «edit».\nВведите команду: ").lower()
    if d == 'exit':
        break
    num += 1
    if d == 'edit':
        print(f'\n Изменения: \n{"_" * 30}')
        for key, value in b.items():
            print(f'{key[:25]:>30}: {value}')
            print("_" * 30)
    for e in a.keys():
        c = input(f'Изменить: "{e}" на: ')
        a[e] = int(c) if (e == 'цена' or e == 'количество') else c
        b[e].append(a[e])
    tovars.append((num, a))
    print(tovars)
    print(a, '\n', b, d)