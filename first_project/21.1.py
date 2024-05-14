"""
Практика
Lesson 21
Собираем данные с учебного сайта books.toscrape.com
"""

from pprint import pprint
from time import sleep
from typing import List, Dict

from selenium import webdriver  # Импорт webdriver.
from selenium.webdriver.common.by import By  # Инструмент By.
from selenium.common.exceptions import NoSuchElementException  # Исключение NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
# from tabulate import tabulate

URL: str = 'http://books.toscrape.com/catalogue/page-1.html'


def get_driver() -> webdriver.Chrome:
    """
    Создание драйвера с настройками
    :return:  webdriver.Chrome
    """
    options: webdriver.ChromeOptions = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")  # Развернуть на весь экран
    return webdriver.Chrome(options=options)


def get_page(url: str, driver: webdriver.Chrome) -> None:
    """
    Переход на страницу
    :param url: str
    :param driver: webdriver.Chrome
    :return: None
    """
    driver.get(url)


def get_all_product_pods_on_page(driver: webdriver.Chrome) -> List[WebElement]:
    """
    Получение всех карточек товаров на странице
    :param driver: webdriver.Chrome
    :return: List[WebElement]
    """
    return driver.find_elements(By.CSS_SELECTOR, '.product_pod')


def get_all_data_from_product_pod(product_pod: WebElement) -> Dict[str, str]:
    """
    Принимает на вход WebElement карточки товара и возвращает словарь с данными по ней
    :param product_pod: WebElement
    :return: Dict[str, str]
    """
    # Название и ссылка лежат в h3 a
    h3_element: WebElement = product_pod.find_element(By.CSS_SELECTOR, 'h3')
    a_element: WebElement = h3_element.find_element(By.CSS_SELECTOR, 'a')
    title: str = a_element.get_attribute('title')
    link: str = a_element.get_attribute('href')

    # Цена лежит в p.price_color
    price_element: WebElement = product_pod.find_element(By.CSS_SELECTOR, 'p.price_color')
    price: str = price_element.text

    # Рейтинг лежит в p.star-rating (Классы One Two Three Four Five)
    rating_element: WebElement = product_pod.find_element(By.CSS_SELECTOR, 'p.star-rating')
    # Достаем классы. Последний - это рейтинг
    rating: str = rating_element.get_attribute('class').split(' ')[-1]
    return {
        'title': title,
        'link': link,
        'price': price,
        'rating': rating
    }


def get_page_count(driver: webdriver.Chrome) -> int:
    """
    Получение количества страниц
    :param driver: webdriver.Chrome
    :return: int
    """
    # Находим элемент li.current - последний элемент с конца - это номер последней страницы
    current_element: WebElement = driver.find_element(By.CSS_SELECTOR, 'li.current')
    last_page_number: int = int(current_element.text.split(' ')[-1])
    return last_page_number


def write_to_json(data: List[Dict[str, str]]) -> None:
    """
    Запись данных в json
    :param data: List[Dict[str, str]]
    :return: None
    """
    import json
    with open('data.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


# def get_tabulate_table_from_list_dict(data: List[Dict[str, str]], colwidth: int = 100) -> str:
#     """
#     Получение таблицы Tabulate из списка словарей
#     :param data: List[Dict[str, str]]
#     :param colwidth: int (ширина столбца по умолчанию)
#     :return: str
#     """
#     return tabulate(data, headers='keys', tablefmt='github', colwidth=colwidth)


def main():
    # Создаем драйвер
    driver: webdriver.Chrome = get_driver()

    # Переходим на страницу
    get_page(URL, driver)

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
        product_pods: List[WebElement] = get_all_product_pods_on_page(driver)
        # Перебираем все карточки товаров
        for product_pod in product_pods:
            # Получаем данные по карточке товара
            product_pod_data: Dict[str, str] = get_all_data_from_product_pod(product_pod)
            # Добавляем данные в список
            data.append(product_pod_data)

    # Закрываем драйвер
    driver.close()

    # Выдаем таблицу в консоль
    print(data)

    # Записываем данные в json
    write_to_json(data)


main()
