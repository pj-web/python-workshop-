"""
Работа с вкладками и окнами в Python Selenium.
"""

import csv
import json
import time
from pprint import pprint
from typing import List, Dict
import undetected_chromedriver as uc

from selenium import webdriver  # Импорт webdriver.
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By  # Инструмент By.
from selenium.common.exceptions import NoSuchElementException  # Исключение NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement

WEB_DRIVER_OPTIONS = ['--start-maximized']

LOCAL_PAGE = r'https://www.dns-shop.ru/catalog/17a8943716404e77/monitory/?order=6'
URL = 'https://www.dns-shop.ru/catalog/17a8943716404e77/monitory/?order=6'
URL_MAIN = 'https://www.dns-shop.ru/'
LOCAL_PAGE_PROMPT = r'D:\PycharmProjects\First_project\23.html'
SULPAK_MAIN_PAGE = r'https://www.sulpak.kz'
BOOK_TO_SCRAPE = r'http://books.toscrape.com/catalogue/page-1.html'
BOOKS_CARD = r'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'


def get_driver(driver_options: list) -> webdriver.Chrome:
    """
    Создание драйвера с настройками
    :return:  webdriver.Chrome
    """
    if driver_options is None:
        driver_options = WEB_DRIVER_OPTIONS
    if driver_options:
        options: webdriver.ChromeOptions = webdriver.ChromeOptions()
        for option in driver_options:
            options.add_argument(option)
        return webdriver.Chrome(options=options)
    else:
        return webdriver.Chrome()


def get_uc_driver(driver_settings: list, ) -> webdriver.Chrome:
    """
    Функция, которая возвращает драйвер селениума в обвертке undetected_chromedriver
    """
    # Создание объекта опций
    options = uc.ChromeOptions()

    for option in driver_settings:
        options.add_argument(option)

    driver = uc.Chrome(options=options)
    return driver


# driver: webdriver.Chrome = get_driver(WEB_DRIVER_OPTIONS)
#
# # Переход на страницу books.toscrape.com
# driver.get(BOOK_TO_SCRAPE)
#
# # Получение всех открытых вкладок в список
# # список идентификаторов
# tabs: List[str] = driver.window_handles
#
# print(tabs)
#
# time.sleep(5)
#
# # Открытие новой вкладки
# # execute_script - выполнение js кода
# # window.open('') - открыть новую вкладку
# driver.execute_script("window.open('');")
#
# # Переход на страницу книги
# driver.switch_to.window(driver.window_handles[1])
# driver.get(BOOKS_CARD)
#
#
# # Получение всех открытых вкладок в список
# # список идентификаторов
# tabs: List[str] = driver.window_handles
#
# print(tabs)
#
# # Получение title страницы
# title: str = driver.title
# print(title)
#
# # Получить идентификатор текущей вкладки
# current_tab: str = driver.current_window_handle
#
# # Получить идентификаторы всех открытых вкладок
# window_handles: List[str] = driver.window_handles
#
# # Переключение на вкладку по идентификатору
# for handle in window_handles:
#     # Переключиться на вкладку
#     driver.switch_to.window(handle)
#     print(f'Перешли на вкладку title: {driver.title}\n'
#           f'Идентификатор вкладки: {handle}')
#     time.sleep(5)
#     driver.close()
#     # Проверить title вкладки
#     # if driver.title == "Искомый Title":
#     #     # Если title совпадает, то выйти из цикла
#     #     break
#

# Таким образом мы можем
"""
1. Открыть много вкладок
2. Для каждой вкладки получить title / идентификатор
3. Собрать к примеру словарь где ключ будет идентификатор, а значение title
4. Переключатся между ними по необходимости"""




#############################################################
# Работа с окнами браузера

driver: webdriver.Chrome = get_driver(WEB_DRIVER_OPTIONS)

# Открываем первое окно (по умолчанию уже открыто)
driver.get(BOOK_TO_SCRAPE)
time.sleep(2)

# Сохраняем идентификатор первого окна
first_window = driver.current_window_handle
time.sleep(2)
# Открываем новое окно
driver.execute_script("window.open('about:blank', 'secondwindow');")
time.sleep(2)
# Переключаемся на новое окно
second_window = [window for window in driver.window_handles if window != first_window][0]
driver.switch_to.window(second_window)
time.sleep(2)
# Переключаемся обратно на первое окно
driver.switch_to.window(first_window)
time.sleep(2)
# Снова переключаемся на второе окно
driver.switch_to.window(second_window)
time.sleep(2)


