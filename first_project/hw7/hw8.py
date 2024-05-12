# Ссылка на скриншот https://prnt.sc/sOiyq96uajcd, для теста html файл загружен на хостинг
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from typing import List

# Локальный файл на Windows
# LOCAL_FILE: str = r'D:\_code\_Python\python-workshop-\first_project_html\index.html'

# Тот же файл на Mac'е
# LOCAL_FILE_MAC: str = 'file:///Users/ivanovpavel/_myFiles/python-workshop-/first_project_html/index.html'

# То же файл на хостинге
HOSTING_FILE: str = 'https://cd15970.tmweb.ru/'


# Создание драйвера с настройками
def get_driver() -> webdriver.Chrome:
    options: webdriver.ChromeOptions = webdriver.ChromeOptions()
    # options.add_argument("--start-maximized")  # Развернуть на весь экран
    options.add_argument("--disable-gpu")  # disable GPU
    options.add_argument("--headless=new")  # отключение отображения браузера
    return webdriver.Chrome(options=options)


# Переход на страницу url
def get_page(url: str, driver: webdriver.Chrome) -> None:
    driver.get(url)


# Печать элементов списка построчно
def print_items(list_of_items: List[WebElement], attr=''):
    for item in list_of_items:
        print(item.text)
        # Если элемент содержит атрибут указанный в аргументе attr,
        # тогда печатает содержание атрибута
        if item.get_attribute(attr):
            print(item.get_attribute(attr))


def main():
    # Создаем драйвер
    driver: webdriver.Chrome = get_driver()

    # Переходим на страницу
    get_page(HOSTING_FILE, driver)

    # Распечатываем построчно полученный текст из параграфов
    print_items(driver.find_elements(By.TAG_NAME, 'p'))

    # Распечатываем построчно полученный текст из списков
    print_items(driver.find_elements(By.TAG_NAME, 'li'))

    # Распечатываем построчно полученный текст из ссылок и содержимое атрибута href
    print_items(driver.find_elements(By.TAG_NAME, 'a'), 'href')


main()
