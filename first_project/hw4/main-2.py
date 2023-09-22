from cities import cities

cities_set = set()
for city_name in cities:
    cities_set.add(city_name["name"])

print(cities_set)
print(f'1: {len(cities_set)}')

user_input = input('Пользовательский ввод: ')

if user_input == 'стоп':
    print('Вы сдались!')
elif user_input[-1] == 'ь' or user_input[-1] == 'ы':
    user_input = input('Введите другое название: ')
else:
    if user_input in cities_set:
        cities_set.remove(user_input)
        print(f'2: {len(cities_set)}')

for city in list(cities_set):
    if city[0] == user_input[-1].upper() and city[-1] != 'ь' and city[-1] != 'ы':
        cities_set.remove(city)
        user_input = input(f'Город {city}, ваш вариант на {city[-1].upper()}: ')
        if user_input in cities_set and user_input[0] == city[-1].upper():
            cities_set.remove(user_input)
            print(f'4: {len(cities_set)} правильно')
        elif user_input == 'стоп':
            print('Вы сдались!')
            break
        else:
            print('Неправильно, вы проиграли!')
            break
