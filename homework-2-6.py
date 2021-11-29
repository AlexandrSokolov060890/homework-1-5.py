goods = []
features = {'Название': '', 'Цена': '', 'Количество': '', 'Ед. измерения': ""}
analytics = {'Название': [], 'Цена': [], 'Количество': [], 'Ед. измерения': []}
num = 0
feature_ = None
control = None
while True:
    control = input("Для выхода нажмите 'Q', для продолжения 'Enter', для аналитики 'A'").upper()
    if control == 'Q':
        break
    num += 1
    if control == 'A':
        print(analytics)
        print(f'\n Итоговая аналитика \n {"/" * 30}')
        for key, value in analytics.items():
            if key != 'unit':
                print(f'{key[:25]:>30}: {value}')
                print("/" * 30)
            else:
                print(f'{key[:25]:>30}: {list(set(value))}')
        break
    for f in features.keys():
        feature_ = input(f'Input feature "{f}"')
        features[f] = int(feature_) if (f == 'price' or f == 'quantity') else feature_
        analytics[f].append(features[f])
    goods.append((num, features))
