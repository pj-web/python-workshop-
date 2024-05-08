from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from typing import List, Dict

LOCAL_FILE = 'file:///Users/ivanovpavel/_myFiles/python-workshop-/first_project_html/index.html'

# То же файл лежит на хостинге. Можно для тестов использовать эту ссылку/переменную
HOSTING_FILE = 'https://cd15970.tmweb.ru/'


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


# Получение всех параграфов на странице
def get_all_paragraphs_on_page(driver: webdriver.Chrome) -> List[WebElement]:
    return driver.find_elements(By.TAG_NAME, 'p')


# Получение всех элементов списка на странице
def get_all_listitems_on_page(driver: webdriver.Chrome) -> List[WebElement]:
    return driver.find_elements(By.TAG_NAME, 'li')
