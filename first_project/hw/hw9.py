from selenium import webdriver  # Импорт webdriver
from selenium.webdriver.common.by import By  # Инструмент By.
from selenium.webdriver.remote.webelement import WebElement
from typing import List

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
def get_page(url: str, driver: webdriver.Chrome) -> None:
    driver.get(url)


# Находим все элементы с классом заданным в аргументе, по умолчанию 'product_pod'
def get_all_class_names(attribute_value: str = 'product_pod'):
    driver: webdriver.Chrome = get_driver(WEB_DRIVER_OPTIONS)
    get_page(URL, driver)
    all_class_names: List[WebElement] = driver.find_elements(By.CLASS_NAME,  attribute_value)
    return all_class_names


def main():

    # Находим все продуктовые карточки на странице по имени класса
    # product_pods: List[WebElement] = driver.find_elements(By.CLASS_NAME, 'product_pod')
    print(get_all_class_names())


main()
