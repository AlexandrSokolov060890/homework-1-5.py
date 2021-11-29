list= input("Введите элементы для списка: ").split()
list[:-1:2], list[1::2] = list[1::2], list[:-1:2]
print(list)
