from time import sleep

from selenium import webdriver  # Импорт webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By  # Инструмент By.

WEB_DRIVER_OPTIONS = ['--start-maximized', '--disable-blink-features=AutomationControlled']
URL = 'https://v15.skladchik.org'


# Создание драйвера с настройками
def get_driver(driver_options: list) -> webdriver.Chrome:
    if driver_options is None:
        driver_options = WEB_DRIVER_OPTIONS
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


driver: webdriver.Chrome = get_driver(WEB_DRIVER_OPTIONS)


def remember_me():
    # Ищем элемент чекбокса "Запомнить меня"
    checkbox_remember_me = driver.find_element(By.ID, "ctrl_remember")

    # Проверяем, установлена ли галочка
    is_checked = checkbox_remember_me.get_attribute("checked")

    # Если галочка "Запомнить меня" не установлена, кликаем по чекбоксу
    if not is_checked:
        checkbox_remember_me.click()
        print("Чекбокс Запомнить меня не был отмечен. Осуществлен клик.")
    else:
        print("Чекбокс Запомнить меня уже отмечен. Действие пропущено.")


def log_in():
    # Нажимаем кнопку "Вход"
    driver.find_element(By.XPATH, '//*[@id="navigation"]/div/nav/div/ul[2]/li[1]/label/a').click()
    # Вводил логин
    driver.find_element(By.XPATH, '//*[@id="LoginControl"]').send_keys("placeholder@placeholder.com")
    # Вводил пароль
    driver.find_element(By.XPATH, '//*[@id="ctrl_password"]').send_keys("placeholder")
    # Нажимаем на кнопку "Вход"
    driver.find_element(By.XPATH, '//*[@id="login"]/div/dl[3]/dd/input').click()


def two_factor_authentication():
    # Проверяем, наличие элемента двухфакторной аутентификации
    try:
        element_2fa = driver.find_element(By.ID, 'ctrl_totp_code')

    except NoSuchElementException:
        print("Двухфакторная аутентификация не требуется.")
        # В том случае, если исключения не возникло, просим пользователя ввести код
    else:
        code_2fa = input('Введите код двухфакторной аутентификации: ')
        element_2fa.send_keys(code_2fa)
        # Ищем элемент чекбокса "Добавить это устройство к доверенным на 30 дней"
        checkbox_trust = driver.find_element(
            By.XPATH, '//*[@id="content"]/div/div/form/dl[3]/dd/ul/li/label/input')

        # Проверяем, установлена ли галочка "Добавить это устройство к доверенным на 30 дней"
        is_checked = checkbox_trust.get_attribute("checked")

        # Если галочка "Добавить это устройство к доверенным на 30 дней" не установлена, кликаем по чекбоксу
        if not is_checked:
            checkbox_trust.click()
            print('Чекбокс "Запомнить меня" не был отмечен. Осуществлен клик.')
        else:
            print('Чекбокс "Запомнить меня" уже отмечен. Действие пропущено.')
        # Нажимаем кнопку "Подтвердить"
        driver.find_element(By.XPATH, '//*[@id="content"]/div/div/form/dl[4]/dd/input').click()


def enter_code_pin(code_pin: str = '0000') -> None:
    # Проверяем, наличие элемента для проверки пин-кода
    try:
        check_code_pin = driver.find_element(By.XPATH, '//*[@id="ctrl_pin_code"]')

    except NoSuchElementException:
        print("Ввод пин-кода не требуется.")
    else:
        check_code_pin.send_keys(code_pin)
        # Ищем элемент чекбокса "Добавить это устройство к доверенным на 30 дней"
        checkbox_trust = driver.find_element(
            By.XPATH, '//*[@id="content"]/div/div/form/dl[3]/dd/ul/li/label/input')

        # Проверяем, установлена ли галочка "Добавить это устройство к доверенным на 30 дней"
        is_checked = checkbox_trust.get_attribute("checked")

        # Если галочка "Добавить это устройство к доверенным на 30 дней" не установлена, кликаем по чекбоксу
        if not is_checked:
            checkbox_trust.click()
            print('Чекбокс "Запомнить меня" не был отмечен. Осуществлен клик.')
        else:
            print('Чекбокс "Запомнить меня" уже отмечен. Действие пропущено.')
        # Нажимаем кнопку "Подтвердить"
        driver.find_element(By.XPATH, '//*[@id="content"]/div/div/form/dl[4]/dd/input').click()


def main():
    get_page(URL, driver)
    sleep(1)

    remember_me()
    sleep(1)

    log_in()
    sleep(2)

    two_factor_authentication()
    sleep(3)

    enter_code_pin()
    sleep(10)


main()
