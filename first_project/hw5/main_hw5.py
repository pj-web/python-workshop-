from cities_hw5 import cities


# функция для получения множества из значений словаря по ключам
def dictionary_to_set(dictionary_input: dict, dict_key: str) -> set[str]:
    output_set = set()
    for key in dictionary_input:
        output_set.add(key[dict_key].lower())
    return output_set


# получаем названия городов из импортированного списка словарей
cities_db = dictionary_to_set(cities, "name")

print(cities_db)


user_input: str = input('Ведите название города, \nбез Ь, Ы, Й на конце: ').lower()


# проверяем полученное название первого города, от которого будем отталкиваться в основном цикле
def initial_input_check(input_argument: str):
    if input_argument == 'стоп':
        print('Мы еще не начали, а вы уже сдались!')
        exit()
    # проверяем чтобы слова не заканчивались на 'ь' 'ы' 'й'
    elif input_argument[-1] == 'ь' or input_argument[-1] == 'ы' or input_argument[-1] == 'й':
        user_input_argument = input('Введите другое название: ').lower()
    else:
        if input_argument in cities_db:  # проверяем наличие введенного названия во множестве
            cities_db.remove(input_argument)  # удаляем введенное название из множества
            print(f'Мой вариант на {input_argument[-1].upper()}')


initial_input_check(user_input)

# основной цикл игры
for city in list(cities_db):
    # выбираем название города для хода компьютера
    if (city in cities_db and city[0] == user_input[-1] and city[-1] != 'ь' and city[-1] != 'ы'
            and city[-1] != 'й'):
        cities_db.remove(city)  # удаляем выбранное название из множества городов
        # компьютер делает ход и предлагает пользователю сделать следующий ход
        user_input = input(f'Город {city.capitalize()}, ваш вариант на {city[-1].upper()}: ').lower()
        # проверяем следующий ход пользователя
        if (user_input in cities_db and user_input[0] == city[-1]
                and user_input[-1] != 'ь' and user_input[-1] != 'ы' and user_input[-1] != 'й'):
            cities_db.remove(user_input)
            print(f'Хороший ход, теперь мой вариант на {user_input[-1].capitalize()}')
        elif user_input == 'стоп':
            print('Вы сдались!')
            break
        else:
            print(f'{user_input.capitalize()} не подходит! Вы проиграли!')
            break
