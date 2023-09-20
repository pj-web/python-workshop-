# Первый вариант решения
# Константы
THRESHOLD_DIGITS = 1
THRESHOLD_UPPER = 1
THRESHOLD_LOWER = 1
THRESHOLD_LEN = 8
# Cчетчики для проверки
digit_counter = 0
upper_counter = 0
lower_counter = 0

input_password = input("Введите пароль: ")

# проверка чтобы пароль не был меньше числа заданного в переменной THRESHOLD_LEN
if len(input_password) >= THRESHOLD_LEN:
    for char in input_password:
        # поверка содержит ли пароль цифры
        if char.isdigit():
            digit_counter += 1
        # поверка содержит ли пароль заглавные буквы
        elif char.isupper():
            upper_counter += 1
        # поверка содержит ли пароль строчные буквы
        elif char.islower():
            lower_counter += 1
    # проверка на соответствие всем трем условиям
    if (digit_counter >= THRESHOLD_DIGITS and upper_counter >= THRESHOLD_UPPER
            and lower_counter >= THRESHOLD_LOWER):
        print(f"Пароль '{input_password}' надежный")
    else:
        print(f"Пароль '{input_password}' не надежный")
else:
    print(f"Пароль '{input_password}' не надежный слишком короткий")
