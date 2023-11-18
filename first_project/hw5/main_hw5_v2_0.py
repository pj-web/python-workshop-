from cities_hw5 import cities

# получаем названия городов из импортированного списка словарей
cities_set = set()
for city_name in cities:
    cities_set.add(city_name["name"])
print(cities_set)

# cities_set = {city["name"].lower() for city in cities if (city["name"][-1] != 'ь' and city["name"][-1] != 'ы'
#               and city["name"][-1] != 'й')}

# cities_set = {city["name"].lower() for city in cities}
#
# print(cities_set)

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












# # функция, которая получает множество из значений словаря по заданному ключу
# def dictionary_to_set(dictionary_input: dict, dict_key: str) -> set[str]:
#     output_set = set()
#     for key in dictionary_input:
#         output_set.add(key[dict_key].lower())
#     return output_set
#
#
# # функция, которая проверяет первое введенное пользователем название города
# def initial_input_check(initial_input: str, source_db: set, stop_word: str):
#     while initial_input[-1] == 'ь' or initial_input[-1] == 'ы' or initial_input[-1] == 'й':
#         initial_input = input('Введите другое название, без Ь, Ы, Й на конце: ').lower()
#     else:
#         if initial_input == stop_word:
#             print('Мы еще не начали, а вы уже сдались!')
#             exit()
#         elif (initial_input in source_db
#               and initial_input[-1] != 'ь' or initial_input[-1] != 'ы' or initial_input[-1] != 'й'):
#             # проверяем наличие введенного названия во множестве
#             source_db.remove(initial_input)  # удаляем введенное название из множества
#             print(f'Мой вариант на {initial_input[-1].upper()}')
#             return initial_input
#
#
# # основной цикл игры
# def the_game(input_db: set, next_input: str, stop_word: str):
#     for city in list(input_db):
#         # выбираем название города для хода компьютера
#         if (city in input_db and city[0] == next_input[-1] and city[-1] != 'ь' and city[-1] != 'ы'
#                 and city[-1] != 'й'):
#             input_db.remove(city)  # удаляем выбранное название из множества городов
#             # компьютер делает ход и предлагает пользователю сделать следующий ход
#             next_input = input(f'Город {city.capitalize()}, ваш вариант на {city[-1].upper()}: ').lower()
#             # проверяем следующий ход пользователя
#             while next_input[-1] == 'ь' or next_input[-1] == 'ы' or next_input[-1] == 'й':
#                 next_input = input('Введите другое название, без Ь, Ы, Й на конце: ').lower()
#             else:
#                 if (next_input in input_db and next_input[0] == city[-1]
#                         and next_input[-1] != 'ь' and next_input[-1] != 'ы' and next_input[-1] != 'й'):
#                     input_db.remove(next_input)
#                     print(f'Хороший ход, теперь мой вариант на {next_input[-1].capitalize()}')
#                 elif next_input == stop_word:
#                     print('Вы сдались!')
#                     break
#                 else:
#                     print(f'{next_input.capitalize()} не подходит! Вы проиграли!')
#                     break
#
#
# def main(imported_dict: dict, dict_key: str, stop_word: str):
#     cities_db = dictionary_to_set(imported_dict, dict_key)
#     user_input: str = input('Ведите название города, \nбез Ь, Ы, Й на конце: ').lower()
#     user_input: str = initial_input_check(user_input, cities_db, stop_word)
#     the_game(cities_db, user_input, stop_word)
#
#
# main(cities, "name", "стоп")
