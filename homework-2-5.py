list = [7, 4, 3, 2]
num = int(input("Введите число (100-Выход): "))
sum = list.count(num)
while num != 100:
    for el in list:
        if sum > 0:
            i = list.index(num)
            list.insert(i+sum, num)
            break
        else:
            if num > el:
                j = list.index(el)
                list.insert(j, num)
                break
            elif num < list[-1]:
                list.append(num)
    print(list)
    num = int(input("Введите новое число (100-Выход): "))