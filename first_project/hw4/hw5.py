from cities import cities

# получаем названия городов из импортированного списка словарей


def cities_to_set() -> set():
    cities_set = set()
    for city_name in cities:
        cities_set.add(city_name["name"].lower())
    return cities_set


print(cities_to_set())


user_input = input('Ведите название города, \nбез Ь, Ы, Й на конце: ').lower()

# проверяем полученное название первого города, от которого будем отталкиваться в основном цикле
if user_input == 'стоп':
    print('Мы еще не начали, а вы уже сдались!')
    exit()
# проверяем чтобы слова не заканчивались на 'ь' 'ы' 'й'
elif user_input[-1] == 'ь' or user_input[-1] == 'ы' or user_input[-1] == 'й':
    user_input = input('Введите другое название: ').lower()
else:
    if user_input in cities_to_set():  # проверяем наличие введенного названия во множестве
        cities_to_set().remove(user_input)  # удаляем введенное название из множества
        print(f'Мой вариант на {user_input[-1].upper()}')

# основной цикл игры
for city in list(cities_to_set()):
    # выбираем название города для хода компьютера
    if (city in cities_to_set() and city[0] == user_input[-1] and city[-1] != 'ь' and city[-1] != 'ы'
            and city[-1] != 'й'):
        cities_to_set().remove(city)  # удаляем выбранное название из множества городов
        # компьютер делает ход и предлагает пользователю сделать следующий ход
        user_input = input(f'Город {city.capitalize()}, ваш вариант на {city[-1].upper()}: ').lower()
        # проверяем следующий ход пользователя
        if (user_input in cities_to_set() and user_input[0] == city[-1]
                and user_input[-1] != 'ь' and user_input[-1] != 'ы' and user_input[-1] != 'й'):
            cities_to_set().remove(user_input)
            print(f'Хороший ход, теперь мой вариант на {user_input[-1].capitalize()}')
        elif user_input == 'стоп':
            print('Вы сдались!')
            break
        else:
            print(f'{user_input.capitalize()} не подходит! Вы проиграли!')
            break
