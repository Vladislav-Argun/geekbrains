the_list = [0]
num = int(input("Введите число: "))
while True:
    for a in range(len(the_list)):
        if the_list[a] == num:
            the_list.insert(a + 1, num)
            break

        elif the_list[a] > num and the_list[a + 1] < num:
            the_list.insert(a + 1, num)

        elif the_list[0] < num:
            the_list.insert(0, num)

        elif the_list[-1] > num:
            the_list.append(num)

    print(f"Ваш список: {the_list}")
    num = int(input("Введите число: "))