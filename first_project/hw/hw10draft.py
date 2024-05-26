from time import sleep

from selenium import webdriver  # Импорт webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By  # Инструмент By.
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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


# Левый клик мышью
def left_click(element: WebElement) -> None:
    element.click()


driver: webdriver.Chrome = get_driver(WEB_DRIVER_OPTIONS)


get_page(URL, driver)
# Нажимаем кнопку "Вход"
driver.find_element(By.XPATH, '//*[@id="navigation"]/div/nav/div/ul[2]/li[1]/label/a').click()
# Ждем 3 секунды
sleep(3)

# Ищем элемент чекбокса "Запомнить меня"
checkbox_remember_me = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ctrl_remember")))

# Проверяем, установлена ли галочка
is_checked = checkbox_remember_me.get_attribute("checked")

# Если галочка "Запомнить меня" не установлена, кликаем по чекбоксу
if not is_checked:
    checkbox_remember_me.click()
    print("Чекбокс Запомнить меня не был отмечен. Осуществлен клик.")
else:
    print("Чекбокс Запомнить меня уже отмечен. Действие пропущено.")

driver.find_element(By.XPATH, '//*[@id="LoginControl"]').send_keys("dr.gonzo.mail71@gmail.com")
# Ждем 1 секунду
sleep(1)
# //*[@id="LoginControl"]
# /html/body/div[1]/div/div/div/div/form/div/dl[1]/dd/input

driver.find_element(By.XPATH, '//*[@id="ctrl_password"]').send_keys("!sc!PJ!41779!")
# //*[@id="ctrl_password"]
# /html/body/div[1]/div/div/div/div/form/div/dl[2]/dd/ul/li[3]/input
# //*[@id="login"]/div/dl[3]/dd/label Запомнить меня

# Нажимаем на кнопку "Вход"
driver.find_element(By.XPATH, '//*[@id="login"]/div/dl[3]/dd/input').click()
sleep(3)


# Нажимаем кнопку для выбора подтверждения по пин-коду
driver.find_element(By.XPATH, '//*[@id="content"]/div/div/form/div/div/a[1]').click()
sleep(2)

# Проверяем, наличие элемента двухфакторной аутентификации
try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ctrl_totp_code")))
    code_2fa = input('Введите код двухфакторной аутентификации: ')
    driver.find_element(By.XPATH, '//*[@id="ctrl_totp_code"]').send_keys(code_2fa)
    # Ищем элемент чекбокса "Добавить это устройство к доверенным на 30 дней"
    checkbox_trust = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="content"]/div/div/form/dl[3]/dd/ul/li/label/input')
    ))
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
except TimeoutException:
    print("Двухфакторная аутентификация не требуется.")


# driver.find_element(By.XPATH, '//*[@id="ctrl_totp_code"]').send_keys(code_2fa)
sleep(5)


# Проверяем, наличие элемента для проверки пин-кода
# try:
#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ctrl_pin_code")))
#     code_pin = '0725'
#     driver.find_element(By.XPATH, '//*[@id="ctrl_pin_code"]').send_keys(code_pin)
#     # Ищем элемент чекбокса "Добавить это устройство к доверенным на 30 дней"
#     checkbox_trust = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
#         (By.XPATH, '//*[@id="content"]/div/div/form/dl[3]/dd/ul/li/label/input')
#     ))
#     # Проверяем, установлена ли галочка "Добавить это устройство к доверенным на 30 дней"
#     is_checked = checkbox_trust.get_attribute("checked")
#
#     # Если галочка "Добавить это устройство к доверенным на 30 дней" не установлена, кликаем по чекбоксу
#     if not is_checked:
#         checkbox_trust.click()
#         print('Чекбокс "Запомнить меня" не был отмечен. Осуществлен клик.')
#     else:
#         print('Чекбокс "Запомнить меня" уже отмечен. Действие пропущено.')
#     # Нажимаем кнопку "Подтвердить"
#     driver.find_element(By.XPATH, '//*[@id="content"]/div/div/form/dl[4]/dd/input').click()
# except TimeoutException:
#     print("Ввод пин-кода не требуется.")


# Проверяем, наличие элемента для проверки пин-кода
try:
    # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ctrl_pin_code")))
    code_pin = '0725'
    driver.find_element(By.XPATH, '//*[@id="ctrl_pin_code"]').send_keys(code_pin)
    # Ищем элемент чекбокса "Добавить это устройство к доверенным на 30 дней"
    checkbox_trust = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/form/dl[3]/dd/ul/li/label/input')

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
except TimeoutException:
    print("Ввод пин-кода не требуется.")


sleep(20)
