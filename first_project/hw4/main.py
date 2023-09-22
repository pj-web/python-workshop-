from cities import cities

# получаем названия городов из импортированного списка словарей
cities_set = set()
for city_name in cities:
    cities_set.add(city_name["name"])
print(cities_set)

user_input = input('Ведите название города: ').capitalize()

for city in list(cities_set):

    if user_input in cities_set:
        cities_set.remove(user_input)
        print(f'Мой вариант на {user_input[-1].capitalize()}')
    elif user_input[-1] == 'ь' or user_input[-1] == 'ы' or user_input[-1] == 'й':
        user_input = input('Введите другое название: ').capitalize()
    if user_input == 'Стоп':
        print('Мы еще не начали, а вы уже сдались!')
        break

    # выбираем название для хода компьютера
    if city[0] == user_input[-1].upper() and city[-1] != 'ь' and city[-1] != 'ы' and city[-1] != 'й':
        cities_set.remove(city)
        user_input = input(f'Город {city}, ваш вариант на {city[-1].upper()}: ').capitalize()
        # проверяем следующий ход пользователя
        if user_input in cities_set and user_input[0] == city[-1].upper():
            cities_set.remove(user_input)
            print(f'Хороший ход, теперь мой вариант на {user_input[-1].capitalize()}')
        elif user_input == 'Стоп':
            print('Вы сдались!')
            break
        else:
            print(f'{user_input} не подходит! Вы проиграли!')
            break
