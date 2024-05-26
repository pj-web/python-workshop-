from time import sleep

from selenium import webdriver  # Импорт webdriver
from selenium.webdriver.common.by import By  # Инструмент By.
from selenium.webdriver.remote.webelement import WebElement

WEB_DRIVER_OPTIONS = ['--start-maximized']
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


# /html/body/div[1]/div/div/div/div/form/div/dl[1]/dd/input
# //*[@id="LoginControl"]
#
# /html/body/div[1]/div/div/div/div/form/div/dl[2]/dd/ul/li[3]/input
# //*[@id="ctrl_password"]


driver: webdriver.Chrome = get_driver(WEB_DRIVER_OPTIONS)


get_page(URL, driver)
# Нажимаем кнопку "Вход"
print(driver.find_element(By.XPATH, '//*[@id="navigation"]/div/nav/div/ul[2]/li[1]/label/a').text)
driver.find_element(By.XPATH, '//*[@id="navigation"]/div/nav/div/ul[2]/li[1]/label/a').click()
# После каждого шага джем 3 секунды
sleep(3)

input_login = driver.find_element(By.XPATH, '//*[@id="LoginControl"]').send_keys("dr.gonzo.mail71@gmail.com")
sleep(3)
# //*[@id="LoginControl"]
# /html/body/div[1]/div/div/div/div/form/div/dl[1]/dd/input

driver.find_element(By.XPATH, '//*[@id="ctrl_password"]').send_keys("!sc!PJ!41779!")
# //*[@id="ctrl_password"]
# /html/body/div[1]/div/div/div/div/form/div/dl[2]/dd/ul/li[3]/input

driver.find_element(By.XPATH, '//*[@id="login"]/div/dl[3]/dd/input').click()

sleep(5)
code_2fa = input('Введите код двухфакторной аутентификации: ')
sleep(5)
input_code_2fa = driver.find_element(By.XPATH, '//*[@id="ctrl_totp_code"]')
input_code_2fa.send_keys(code_2fa)
sleep(5)
driver.find_element(By.XPATH, '//*[@id="content"]/div/div/form/dl[3]/dd/ul/li/label/input').click()
driver.find_element(By.XPATH, '//*[@id="content"]/div/div/form/dl[4]/dd/input').click()

# //*[@id="ctrl_totp_code"]
# /html/body/div[1]/div[2]/div/div/form/dl[2]/dd/input