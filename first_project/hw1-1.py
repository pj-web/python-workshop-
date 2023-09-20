# Второй вариант решения без использования цикла
# Константы
THRESHOLD_LEN = 8

input_password = input("Введите пароль: ")

# проверка не является ли пароль более коротким, чем необходимо
if len(input_password) < THRESHOLD_LEN:
    print(f"Пароль '{input_password}' не надежный слишком короткий")
# поверка содержит ли пароль цифры
elif input_password.isalpha():
    print(f"Пароль '{input_password}' не надежный не содержит цифр")
# поверка содержит ли пароль заглавные буквы
elif input_password == input_password.lower():
    print(f"Пароль '{input_password}' не надежный не содержит заглавных букв")
# поверка содержит ли пароль строчные буквы
elif input_password == input_password.upper():
    print(f"Пароль '{input_password}' не надежный не содержит строчных букв")
else:
    print(f"Пароль '{input_password}' надежный")
