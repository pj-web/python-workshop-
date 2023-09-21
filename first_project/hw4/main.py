from cities import cities

cities_set = set()
for city_name in cities:
    cities_set.add(city_name["name"])

print(cities_set)
print(len(cities_set))
used_cities = cities_set.pop()
# print(used_cities)

# user_input = input(f'Мой ход первый: {used_cities}, Введите название города: ')
# print(user_input)

while cities_set:
    user_input = input(f'Введите название города: ')
    while user_input != 'стоп':
        if user_input in cities_set:
            print(len(cities_set))
            last_char = user_input[-1]
            # next_city = {city for city in cities_set if cities_set}
            # used_cities = cities_set.pop()
            for city in cities_set:
                if city[0] == last_char.upper():
                    # print(city)
                    cities_set.discard(city)
                    user_input = input(f'Последняя буква: {last_char}: {city}, ваш ход:  ')
                    break
        # elif user_input not in cities_set:
        #     user_input = input(f'Город {user_input} не подходит! Введите другой: ')
        else:
            user_input = input(f'Город {user_input} не подходит (else)! Введите другой: ')
            break

        #         next_move = [city for city in cities_set if city[0] == last_char]
        # user_input = input(f'Последняя буква {last_char}, Город: {next_city} ')
        # for city in cities_set:
        # if cities_set[0] == last_char:
        #     user_input = input(f'Мой ход {city}')
        # next_move = [city for city in cities_set if city[0] == last_char]

    else:
        print('Ха-ха-ха! Ты проиграл, человек!')
        break




