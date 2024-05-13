from selenium import webdriver  # Импорт webdriver
from selenium.webdriver.common.by import By  # Инструмент By.
from selenium.webdriver.remote.webelement import WebElement
from typing import List, Dict
from pprint import pprint

# Настраиваем драйвер на режим без головы, с отключенным аппаратным ускорением графики
WEB_DRIVER_OPTIONS = ['--disable-gpu', '--headless=new']
URL = 'http://books.toscrape.com/'


# Создание драйвера с настройками
def get_driver(driver_options: list) -> webdriver.Chrome:
    if driver_options:
        options: webdriver.ChromeOptions = webdriver.ChromeOptions()
        for option in driver_options:
            options.add_argument(option)
        return webdriver.Chrome(options=options)
    else:
        return webdriver.Chrome()


# Переход на страницу
def get_page(url: str, web_drv: webdriver.Chrome) -> None:
    web_drv.get(url)


# Создаем Web driver
driver: webdriver.Chrome = get_driver(WEB_DRIVER_OPTIONS)


# 1. Функция для нахождения всех карточек на одной странице.
# Аргумент функции - имя CSS класса, по умолчанию 'product_pod'
def get_all_cards(attribute_value: str = 'product_pod'):
    all_cards: List[WebElement] = driver.find_elements(By.CLASS_NAME,  attribute_value)
    return all_cards


# 2. Функция для извлечения данных из одной карточки, номер карточки вводит пользователь.
def get_data_from_card(input_cards: List[WebElement]):
    index: int = int(input(f'Введите номер карточки (всего их {len(get_all_cards())}): ')) - 1
    result: List[Dict[str, str]] = []

    # Проверяем, чтобы введенное значение было не больше, чем число карточек на странице
    if index <= len(get_all_cards()):
        # Получаем данные из элемента переданного в аргументе index
        title: str = input_cards[index].find_element(By.CSS_SELECTOR, 'h3 a').get_attribute('title')
        url: str = input_cards[index].find_element(By.CSS_SELECTOR, 'h3 a').get_attribute('href')
        img_url: str = input_cards[index].find_element(By.CSS_SELECTOR, 'img').get_attribute('src')
        price: str = input_cards[index].find_element(By.CSS_SELECTOR, '.price_color').text

        # Рейтинг лежит в p.star-rating (Классы One Two Three Four Five)
        rating_element: WebElement = input_cards[index].find_element(By.CSS_SELECTOR, 'p.star-rating')
        # Достаем классы. Последний - это рейтинг
        rating: str = rating_element.get_attribute('class').split(' ')[-1]

        result.append({
            'title': rf"{title}",
            'url': rf"{url}",
            'img_url': rf"{img_url}",
            'price': rf"{price}",
            'rating': rf"{rating}"
        })

        pprint(result)
    else:
        print(f'Нужно значение значение от 0 до {len(get_all_cards())}')


# 3. Функция для извлечения данных со всех карточек на одной странице.
def get_data_from_cards(input_cards: List[WebElement]):
    result: List[Dict[str, str]] = []

    for card in input_cards:
        title: str = card.find_element(By.CSS_SELECTOR, 'h3 a').get_attribute('title')
        url: str = card.find_element(By.CSS_SELECTOR, 'h3 a').get_attribute('href')
        img_url: str = card.find_element(By.CSS_SELECTOR, 'img').get_attribute('src')
        price: str = card.find_element(By.CSS_SELECTOR, '.price_color').text

        # Рейтинг лежит в p.star-rating (Классы One Two Three Four Five)
        rating_element: WebElement = card.find_element(By.CSS_SELECTOR, 'p.star-rating')
        # Достаем классы. Последний - это рейтинг
        rating: str = rating_element.get_attribute('class').split(' ')[-1]

        result.append({
            'title': rf"{title}",
            'url': rf"{url}",
            'img_url': rf"{img_url}",
            'price': rf"{price}",
            'rating': rf"{rating}"
        })

    pprint(result)


# 4. Функция для определения количества страниц на сайте.
def get_page_count(driver: webdriver.Chrome) -> None:

    # Находим последний элемент с конца - это номер последней страницы
    current_element: WebElement = driver.find_element(By.CSS_SELECTOR, 'li.current')
    last_page_number: int = int(current_element.text.split(' ')[-1])
    print(f'Количество страниц: {last_page_number}')


def main():

    get_page(URL, driver)

    get_data_from_card(get_all_cards())

    get_data_from_cards(get_all_cards())

    get_page_count(driver)


main()
