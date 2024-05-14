from selenium import webdriver  # Импорт webdriver
from selenium.webdriver.common.by import By  # Инструмент By.
from selenium.webdriver.remote.webelement import WebElement
from typing import List, Dict
from pprint import pprint

# Настраиваем драйвер на режим без головы, с отключенным аппаратным ускорением графики
WEB_DRIVER_OPTIONS = ['--disable-gpu', '--headless=new']
URL: str = 'http://books.toscrape.com/'
URL_INIT: str = 'http://books.toscrape.com/catalogue/page-1.html'


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
def get_all_cards(driver: webdriver.Chrome):
    return driver.find_elements(By.CLASS_NAME,  'product_pod')


# 2. Функция для извлечения данных из одной карточки, номер карточки вводит пользователь.
def get_data_from_card(input_card: WebElement):

    # Получаем данные из элемента переданного в аргументе
    title: str = input_card.find_element(By.CSS_SELECTOR, 'h3 a').get_attribute('title')
    url: str = input_card.find_element(By.CSS_SELECTOR, 'h3 a').get_attribute('href')
    img_url: str = input_card.find_element(By.CSS_SELECTOR, 'img').get_attribute('src')
    price: str = input_card.find_element(By.CSS_SELECTOR, '.price_color').text

    # Рейтинг лежит в p.star-rating (Классы One Two Three Four Five)
    rating_element: WebElement = input_card.find_element(By.CSS_SELECTOR, 'p.star-rating')
    # Достаем классы. Последний - это рейтинг
    rating: str = rating_element.get_attribute('class').split(' ')[-1]

    return {
        'title': rf"{title}",
        'url': rf"{url}",
        'img_url': rf"{img_url}",
        'price': rf"{price}",
        'rating': rf"{rating}"
    }


# 4. Функция для определения количества страниц на сайте.
def get_page_count(driver: webdriver.Chrome) -> int:

    # Находим последний элемент с конца - это номер последней страницы
    current_element: WebElement = driver.find_element(By.CSS_SELECTOR, 'li.current')
    last_page_number: int = int(current_element.text.split(' ')[-1])
    # print(f'Количество страниц: {last_page_number}')
    return last_page_number


# 3. Функция для извлечения данных со всех карточек на одной странице.
# def get_data_from_cards(input_cards: List[WebElement]):
#     result: List[Dict[str, str]] = []
#
#     for card in input_cards:
#         title: str = card.find_element(By.CSS_SELECTOR, 'h3 a').get_attribute('title')
#         url: str = card.find_element(By.CSS_SELECTOR, 'h3 a').get_attribute('href')
#         img_url: str = card.find_element(By.CSS_SELECTOR, 'img').get_attribute('src')
#         price: str = card.find_element(By.CSS_SELECTOR, '.price_color').text
#
#         # Рейтинг лежит в p.star-rating (Классы One Two Three Four Five)
#         rating_element: WebElement = card.find_element(By.CSS_SELECTOR, 'p.star-rating')
#         # Достаем классы. Последний - это рейтинг
#         rating: str = rating_element.get_attribute('class').split(' ')[-1]
#
#         result.append({
#             'title': rf"{title}",
#             'url': rf"{url}",
#             'img_url': rf"{img_url}",
#             'price': rf"{price}",
#             'rating': rf"{rating}"
#         })
#
#     pprint(result)
#     return result


# Получаем все страницы
def get_all_pages():

    # Переходим на страницу
    get_page(URL_INIT, driver)

    # Получаем количество страниц
    page_count: int = get_page_count(driver)

    # Создаем пустой список для данных
    data: List[Dict[str, str]] = []

    # Перебираем все страницы
    for page_number in range(1, page_count + 1):
        # Получаем ссылку на страницу
        page_url: str = f'http://books.toscrape.com/catalogue/page-{page_number}.html'
        # Переходим на страницу
        get_page(page_url, driver)
        # Проверяем статус код
        # Получаем все карточки товаров на странице
        product_pods: list[WebElement] = get_all_cards(driver)
        # Перебираем все карточки товаров
        for product_pod in product_pods:
            # Получаем данные по карточке товара
            product_pod_data: Dict[str, str] = get_data_from_card(product_pod)
            # Добавляем данные в список
            data.append(product_pod_data)
            print(f'Содержимое страницы № {page_number}:')
            pprint(data)
            print('----------------------------------------------')

    # Закрываем драйвер
    driver.close()


# def main():
#
#     get_page(URL, driver)
#
#     get_data_from_card(get_all_cards())
#
#     get_data_from_cards(get_all_cards())
#
#     get_page_count(driver)
#
#
# main()

get_all_pages()


