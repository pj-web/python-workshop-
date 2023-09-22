from cities import cities

cities_set = set()
for city_name in cities:
    cities_set.add(city_name["name"])

print(cities_set)
print(f'1: {len(cities_set)}')
# first_city = cities_set.pop()
# print(first_city)
# user_input = input(f'Мой первый ход: {first_city} \nВведите город на {first_city[-1].upper()}: ')

# user_input = input(f'Мой ход первый: {used_cities}, Введите название города: ')
# print(user_input)

while cities_set:
    # user_input = input(f'Введите название города: ')
    while user_input != 'стоп':
        if user_input in cities_set:
            cities_set.remove(user_input)
            print(f'2: {len(cities_set)}')
            for city in cities_set:
                if city[0] == user_input[-1].upper():
                    cities_set.remove(city)
                    print(f'3: {len(cities_set)}')
                    user_input = input(f'Последняя буква: {user_input[-1].upper()}: {city}, \n'
                                       f'Ваш ход, введите город на {city[-1].upper()}:  ')
                    # if user_input[0] == city[-1].upper():
                    #     break
                    # else:
                    #     print(f'Не с той буквы, нужна буква {city[-1].upper()}')
                    #     break
        # elif user_input not in cities_set:
        #     user_input = input(f'Город {user_input} не подходит! Введите другой: ')
        else:
            user_input = input(f'Город {user_input} не подходит, еще попытка:  ')
            # print(f'Город {user_input} не подходит (else)!')
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




