from selenium import webdriver


def choose_browser():
    browser_type_input = input('Для какого браузера создать веб-драйвер?\n'
                               'Google Chrome - введите 1\n'
                               'Firefox - введите 2\n'
                               'Edge - введите 3\n'
                               'Введите сюда: ')
    # Выбор браузера в зависимости от введенного пользователем значения:
    if browser_type_input == '1':
        driver = webdriver.Chrome()
    elif browser_type_input == '2':
        driver = webdriver.Firefox()
    elif browser_type_input == '3':
        driver = webdriver.Edge()
    else:
        raise ValueError(f"Ошибка: некорректное значение: {browser_type_input}")

    # Возвращает объект драйвера для управления браузером.
    return driver


# Пример использования функции:
# Создание объекта драйвера исходя введенного выбора пользователя
webdriver_instance = choose_browser()
webdriver_instance.get('http://www.google.com')
