num = input('Введите целое положительное число: ')
numb = int(num)
search = 0
while numb > 10:
    prom = numb % 10
    numb = numb // 10
    if prom > search:
        search = prom
print(search)
