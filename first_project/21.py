"""
Day 21.
Python Selenium.

Знакомство с инструментами на учебных примерах.

1. Driver.get() - переход на страницу
2. Поиск элементов на странице (Инструмент By.)
- webdriver.find_element() - поиск одного элемента
- webdriver.find_elements() - поиск нескольких элементов
- By.ID - поиск по id
- By.CLASS_NAME - поиск по классу
- By.TAG_NAME - поиск по тегу
- By.NAME - поиск по имени
- By.LINK_TEXT - поиск по ссылке
- By.PARTIAL_LINK_TEXT - поиск по части ссылки
- By.CSS_SELECTOR - поиск по селектору
- noSuchElementException - исключение, если элемент не найден

3. text, get_attribute() - получение текста и атрибута элемента
4. click() - клик по элементу
5. send_keys() - ввод текста в элемент
6. back() - возврат на предыдущую страницу
7. sleep() - задержка на время
8. pprint() - красивый вывод


"""
from pprint import pprint
from time import sleep
from typing import List, Dict

from selenium import webdriver # Импорт webdriver.
from selenium.webdriver.common.by import By  # Инструмент By.
from selenium.common.exceptions import NoSuchElementException  # Исключение NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement

LOCAL_FILE = r'D:\PycharmProjects\First_project\19.html'
URL = 'http://books.toscrape.com/'

# Создаем объект для настроек
options: webdriver.ChromeOptions = webdriver.ChromeOptions()

# Добавляем настройки
options.add_argument("--start-maximized")  # Развернуть на весь экран

# Создаем драйвер с настройками
driver: webdriver.Chrome = webdriver.Chrome(options=options)

# Переходим на страницу
# driver.get(LOCAL_FILE)

# FIND ELEMENT и FIND ELEMENTS
# Поиск элемента по имени тега body - возвращает один элемент
# find_element - ищет один элемент. В нем, мы можем использовать все инструменты By. столько раз, сколько нам нужно.
# find_elements - ищет несколько элементов. В нем, мы можем использовать все инструменты By. столько раз, сколько нам нужно.

# Пример работы с инструментом By.TAG_NAME
# body_element: webdriver.remote.webelement.WebElement = driver.find_element(By.TAG_NAME, 'body')
# body_element: WebElement = driver.find_element(By.TAG_NAME, 'body')


# BY.ID - поиск по id ########################################################
# driver.get(LOCAL_FILE)
# Пример работы с инструментом By.ID messages
# divs_blocks: WebElement = driver.find_element(By.ID, '1')
# text_element: str = divs_blocks.text
#
# print(type(divs_blocks))
# print(text_element.split('\n'))

# Погружаемся глубже и ищем элемент с id div-3
# div_3_element: WebElement = divs_blocks.find_element(By.ID, 'div-3')
# text_div3_element: str = div_3_element.text
#
# print(text_div3_element)

# BY.CLASS_NAME - поиск по классу ########################################################

# driver.get(LOCAL_FILE)
# Пример работы с инструментом By.CLASS_NAME
# Ищем элемент с классом flex-container
# divs_block: WebElement = driver.find_element(By.CLASS_NAME, 'flex-container')
# print(divs_block.text)

# Ищем ВСЕ элементы с классом flex-item
# inner_divs: List[WebElement] = divs_block.find_elements(By.CLASS_NAME, 'flex-item')
# print(type(inner_divs))
# print(len(inner_divs))
# print(inner_divs[0].text)

# Мы можем передать только ОДНО имя класса.
# Если элемент имеет несколько классов, то мы не сможем найти его по одному из них.

# BY.CLASS on books.toscrape.com ########################################################
# driver.get(URL)
#
# # Ищем все элементы с классом product_pod
# products_cards: List[WebElement] = driver.find_elements(By.CLASS_NAME, 'product_pod')
#
# # Печатаем в цикле текст каждого элемента
# for product_card in products_cards:
#     print('-------------------')
#     print(product_card.text)


# BY.TAG_NAME - поиск по тегу ########################################################
# driver.get(LOCAL_FILE)

# На учебной странице всего 2 заголовка h2
# h2_elements: List[WebElement] = driver.find_elements(By.TAG_NAME, 'h2')

# Печатаем в цикле текст каждого элемента
# [print(h2_element.text) for h2_element in h2_elements]


# Ищем сначала по имени класса все продуктовые карточки, потом в каждой карточке ищем заголовок h3, складываем в список

# driver.get(URL)
# product_cards: List[WebElement] = driver.find_elements(By.CLASS_NAME, 'product_pod')
#
# # Создаем пустой список для заголовков
# product_titles: List[str] = []
#
# # Перебираем все карточки
# for product_card in product_cards:
#     # Ищем заголовок в каждой карточке
#     title_element: WebElement = product_card.find_element(By.TAG_NAME, 'h3')
#     # Добавляем текст заголовка в список
#     product_titles.append(title_element.text)
#
# # Печатаем список заголовков
# print(product_titles)

# BY.NAME - поиск по имени ########################################################
# driver.get(LOCAL_FILE)
#
# # Ищем элемент с именем firstname
# first_name_element: WebElement = driver.find_element(By.NAME, 'firstname')
# first_name_element.send_keys('Иван')
#
# sleep(10)


# BY.LINK_TEXT - поиск по ссылке ########################################################
# BY.PARTIAL_LINK_TEXT - поиск по части ссылки ##########################################

# TEXT_LINK: str = 'A Light in the ...'
#
# driver.get(URL)
#
# # Ищем элемент с текстом A Light in the Attic
# link_element: WebElement = driver.find_element(By.LINK_TEXT, TEXT_LINK)
# link_element.click()
#
# sleep(5)
#
# # Возвращаемся назад
# driver.back()
# sleep(2)
#
# # ищем элемент с частью текста
# link_element: WebElement = driver.find_element(By.PARTIAL_LINK_TEXT, 'Light in the')
# link_element.click()
#
# sleep(5)

# BY.CSS_SELECTOR - поиск по селектору ########################################################

driver.get(URL)

# Ищем все article.product_pod
product_cards: List[WebElement] = driver.find_elements(By.CSS_SELECTOR, 'article.product_pod')

# Создаем пустой список для заголовков
product_titles: Dict[str, str] = {}

# Перебираем все карточки
for product_card in product_cards:
    # Ищем заголовок в каждой карточке h3 a [title]
    title_element: WebElement = product_card.find_element(By.CSS_SELECTOR, 'h3 a')
    # Добываем заголовок
    title: str = title_element.get_attribute('title')
    # Добываем ссылку
    link: str = title_element.get_attribute('href')
    # Добавляем в словарь
    product_titles.update(
        {
            title: link
        }
    )

# Печатаем список заголовков
pprint(product_titles)


