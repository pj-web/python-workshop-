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
    Функция, которая возвращает драйвер селениума
    """
    # Создание объекта опций
    options = uc.ChromeOptions()

    for option in driver_settings:
        options.add_argument(option)

    driver = uc.Chrome(options=options)
    return driver


def get_page(url: str, driver: webdriver.Chrome) -> None:
    """
    Переход на страницу
    :param url: str
    :param driver: webdriver.Chrome
    :return: None
    """
    driver.get(url)


######

def left_click(element: WebElement) -> None:
    """
    Левый клик мышью
    :param element: WebElement
    :return: None
    """
    element.click()


def right_click(element: WebElement, driver: webdriver.Chrome) -> None:
    """
    Правый клик мышью
    :param driver:
    :param element: WebElement
    :return: None
    """
    webdriver.ActionChains(driver).context_click(element).perform()


def step_back(driver: webdriver.Chrome) -> None:
    """
    Шаг назад
    :param driver: webdriver.Chrome
    :return: None
    """
    driver.back()


def step_forward(driver: webdriver.Chrome) -> None:
    """
    Шаг вперед
    :param driver: webdriver.Chrome
    :return: None
    """
    driver.forward()


def get_refresh(driver: webdriver.Chrome) -> None:
    """
    Обновить страницу
    :param driver: webdriver.Chrome
    :return: None
    """
    driver.refresh()


def press_key(key: Keys, element: WebElement) -> None:
    """
    Нажатие на клавишу
    :param key: Keys
    :param element: WebElement
    :return: None
    """
    element.send_keys(key)


def scroll_mouse_wheel(x: int, y: int, driver: webdriver.Chrome) -> None:
    """
    Прокрутка колеса мыши
    :param x: int
    :param y: int
    :param driver: webdriver.Chrome
    :return: None
    """
    driver.execute_script(f"window.scrollTo({x}, {y});")


def dns_scroll_more_button(driver: webdriver.Chrome) -> None:
    """
    Функция которая будет нажимать Показать ещё до тех пор, пока находится кнопка
    А потом делать скролл вниз на 4000 пикселей

    :param driver:
    :return:
    """
    while True:
        try:
            # Находим button внутри  div id products-list-pagination
            button_more = driver.find_element(By.CSS_SELECTOR, 'div[id="products-list-pagination"] button')
            # Жмем на кнопку
            left_click(button_more)
            time.sleep(3)
        except NoSuchElementException:
            scroll_mouse_wheel(0, 4000, driver)
            break


def main():
    # Создаем UC драйвер
    driver: webdriver.Chrome = get_uc_driver(driver_settings=WEB_DRIVER_OPTIONS)

    # Переходим на страницу
    get_page(URL_MAIN, driver)
    time.sleep(2)

    # Ищем поле поиска input name="q"
    search_input: WebElement = driver.find_element(By.CSS_SELECTOR, 'input[name="q"]')

    # Вводим в поле поиска "монитор"
    search_input.send_keys('монитор')

    # Нажимаем Enter
    press_key(Keys.ENTER, search_input)

    # Спим
    time.sleep(2)

    # Прокрутка вниз колесом мыши на 2000 пикселей
    # scroll_mouse_wheel(0, 4000, driver)

    # Находим button внутри  div id products-list-pagination
    # button_more = driver.find_element(By.CSS_SELECTOR, 'div[id="products-list-pagination"] button')


    # Жмем на кнопку
    # left_click(button_more)

    # Запускаем функцию прокрутки
    dns_scroll_more_button(driver)

    # Спим
    time.sleep(60)

def main_prompt():
    # Создаем обычный драйвер
    driver: webdriver.Chrome = get_driver(driver_options=WEB_DRIVER_OPTIONS)

    # Переходим на локальную страницу
    get_page(LOCAL_PAGE_PROMPT, driver)

    # Ищем кнопку запуска prompt по имени тега
    button_prompt: WebElement = driver.find_element(By.TAG_NAME, 'button')

    # Жмем на кнопку
    left_click(button_prompt)

    # Спим
    time.sleep(5)

    # Переключаемся на prompt
    prompt = driver.switch_to.alert

    # Вводим текст в prompt
    prompt.send_keys('Иван')

    # Нажимаем Enter
    prompt.accept()

    # Спим
    time.sleep(20)

def main_sulpak_form():
    # Создаем uc драйвер
    driver: webdriver.Chrome = get_uc_driver(driver_settings=WEB_DRIVER_OPTIONS)

    # Переходим на страницу
    get_page(SULPAK_MAIN_PAGE, driver)

    # Спим
    time.sleep(2)
    # Ищем кнопку НЕТ (Мой город не Алматы)  a.btn.btn__white-red.btn__medium.btn__block.popup__link-js.select_city.popup-city-link
    # Ищем по селектору
    no_button: WebElement = driver.find_element(By.CSS_SELECTOR, 'a.btn.btn__white-red.btn__medium.btn__block.popup__link-js.select_city.popup-city-link')

    # Жмем на кнопку
    left_click(no_button)

    # Спим
    time.sleep(1)

    # Ищем форму с id  # Форма popup__city-input
    city_form: WebElement = driver.find_element(By.ID, 'popup__city-input')
    time.sleep(1)
    # Вводим в форму Усть-Каменогорск
    city_form.send_keys('Усть-Каменогорск')
    time.sleep(1)
    # Ищем первую поисковую подсказку div.form__input-suggestions-block.form__input-suggestions-items-js
    first_suggestion: WebElement = driver.find_element(By.CSS_SELECTOR, 'div.form__input-suggestions-block.form__input-suggestions-items-js')
    time.sleep(1)
    # Жмем на первую подсказку
    left_click(first_suggestion)
    time.sleep(100)

# main()
# main_prompt()
main_sulpak_form()

