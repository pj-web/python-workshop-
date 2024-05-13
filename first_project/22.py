import csv
import json
import time
from pprint import pprint
from typing import List, Dict

from selenium import webdriver  # Импорт webdriver.
from selenium.webdriver.common.by import By  # Инструмент By.
from selenium.common.exceptions import NoSuchElementException  # Исключение NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement

WEB_DRIVER_OPTIONS = ['--start-maximized']
LOCAL_PAGE = r'D:\PycharmProjects\First_project\22.html'
URL = 'http://books.toscrape.com/'


def get_driver(driver_options: list = WEB_DRIVER_OPTIONS) -> webdriver.Chrome:
    """
    Создание драйвера с настройками
    :return:  webdriver.Chrome
    """
    if driver_options:
        options: webdriver.ChromeOptions = webdriver.ChromeOptions()
        for option in driver_options:
            options.add_argument(option)
        return webdriver.Chrome(options=options)
    else:
        return webdriver.Chrome()


def get_page(url: str, driver: webdriver.Chrome) -> None:
    """
    Переход на страницу
    :param url: str
    :param driver: webdriver.Chrome
    :return: None
    """
    driver.get(url)


def main():
    driver: webdriver.Chrome = get_driver()
    get_page(URL, driver)
    time.sleep(1)

    # Получаем все продуктовые карточки на странице класс .product_pod
    product_pods: List[WebElement] = driver.find_elements(By.CLASS_NAME, 'product_pod')

    # Проходимся по всем карточкам
    result: List[Dict[str, str]] = []

    for product_pod in product_pods:
        title: str = product_pod.find_element(By.CSS_SELECTOR, 'h3 a').get_attribute('title')
        url: str = product_pod.find_element(By.CSS_SELECTOR, 'h3 a').get_attribute('href')
        img_url: str = product_pod.find_element(By.CSS_SELECTOR, 'img').get_attribute('src')
        price: str = product_pod.find_element(By.CSS_SELECTOR, '.price_color').text

        result.append({
            'title': rf"{title}",
            'url': rf"{url}",
            'img_url': rf"{img_url}",
            'price': rf"{price}"
        })

    # Пишем все в JSON с отступами и ensure_ascii=False и json dump
    # with open('result.json', 'w', encoding='utf-8') as file:
    #     json.dump(result, file, indent=4, ensure_ascii=False)
    #
    # # Читаем JSON и сохраняем его в CSV с кодировкой виндовс и разделителем и ньюлайн
    # with open('result.json', 'r', encoding='utf-8') as file:
    #     result = json.load(file)
    #
    # with open('result.csv', 'w', encoding='utf-8', newline='') as file:
    #     writer = csv.writer(file, delimiter=';')
    #     writer.writerow(['title', 'url', 'img_url', 'price'])
    #     for item in result:
    #         writer.writerow([item['title'], item['url'], item['img_url'], item['price']])

    pprint(result)


# Работа с таблицами

# def main():
#     # Создаем драйвер
#     driver: webdriver.Chrome = get_driver()
#     # Переходим на страницу
#     get_page(LOCAL_PAGE, driver)
#     # Получаем тело таблицы
#     table_body: WebElement = driver.find_element(By.TAG_NAME, 'tbody')
#
#     # Получаем заголовки столбцов из thead
#     header: WebElement = driver.find_element(By.TAG_NAME, 'thead')
#     # Получаем все ячейки заголовка
#     header_cells: List[WebElement] = header.find_elements(By.TAG_NAME, 'th')
#
#     # Получаем все строки таблицы
#     rows: List[WebElement] = table_body.find_elements(By.TAG_NAME, 'tr')
#
#     # Создаем пустой список для результатов
#     result: List[List[str]] = []
#
#     # Добавляем в результат список заголовков через list comprehension
#     result.append([cell.text for cell in header_cells])
#
#     # Проходимся по всем строкам
#     for row in rows:
#         # Получаем все ячейки в строке
#         cells: List[WebElement] = row.find_elements(By.TAG_NAME, 'td')
#         # Создаем пустой список для ячеек
#         row_result: List[str] = []
#         # Проходимся по всем ячейкам
#         for cell in cells:
#             # Добавляем текст ячейки в список
#             row_result.append(cell.text)
#         # Добавляем список ячеек в результат
#         result.append(row_result)
#
#     print(result)
#
#     # Пишем в CSV с разделителем и ньюлайн и кодировкой виндовс
#     with open('result_table.csv', 'w', encoding='windows-1251', newline='') as file:
#         writer = csv.writer(file, delimiter=';')
#         for row in result:
#             writer.writerow(row)


main()
