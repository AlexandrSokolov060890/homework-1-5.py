month = int(input("Введите порядковый номер месяца: "))
season_list = ['Зима', 'Весна', 'Лето', 'Осень']
season_dict = {1 : 'Зима', 2 : 'Весна', 3 : 'Лето', 4 : 'Осень'}
if month == 1 or month == 2 or month == 12:
        print(season_dict.get(1))
        print(season_list[0])
elif month == 3 or month == 4 or month == 5:
    print(season_dict.get(2))
    print(season_list[1])
elif month == 6 or month == 7 or month == 8:
    print(season_dict.get(3))
    print(season_list[2])

elif month == 9 or month == 10 or month == 11:
    print(season_dict.get(4))
    print(season_list[3])
else:
        print("Такого месяца не существует!")