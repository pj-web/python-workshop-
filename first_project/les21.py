import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

LOCAL_FILE = 'file:///Users/ivanovpavel/_myFiles/python-workshop-/first_project_html/index.html'
MY_URL = 'https://cd15970.tmweb.ru/'
URL = 'https://books.toscrape.com/'

# создаем объект для настроек
options: webdriver.ChromeOptions = webdriver.ChromeOptions()

# добавляем настройки
options.add_argument("--start-maximized")  # развернуть на весь экран


# создаем драйвер с настройками
driver: webdriver.Chrome = webdriver.Chrome(options=options)


# переходим на страницу
# driver.get(URL)
driver.get(LOCAL_FILE)

# поиск элементов по имени тега body - возвращает один элемент
body_element: webdriver.remote.webelement.WebElement = driver.find_element(By.TAG_NAME, "body")
# body_element: WebElement = driver.find_element(By.TAG_NAME, "body")

print(body_element.text)
