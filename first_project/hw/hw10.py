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
sleep(15)
print(driver.find_element(By.XPATH, '//*[@id="navigation"]/div/nav/div/ul[2]/li[1]/label/a').text)
driver.find_element(By.XPATH, '//*[@id="navigation"]/div/nav/div/ul[2]/li[1]/label/a').click()
# driver.find_element(By.CSS_SELECTOR, '#navigation > div > nav > div > ul.visitorTabs > li:nth-child(1) > label > a').click()
sleep(3)

input_login = driver.find_element(By.XPATH, '//*[@id="LoginControl"]/html/body/div[1]/div/div/div/div/form/div/dl[1]/dd/input')
input_login.send_keys("dr.gonzo.mail71@gmail.com")
sleep(3)
# //*[@id="LoginControl"]
# /html/body/div[1]/div/div/div/div/form/div/dl[1]/dd/input

input_password = driver.find_element(By.XPATH, '//*[@id="ctrl_password"]/html/body/div[1]/div/div/div/div/form/div/dl[2]/dd/ul/li[3]/input')
input_password.send_keys("dr.gonzo.mail71@gmail.com")
# //*[@id="ctrl_password"]
# /html/body/div[1]/div/div/div/div/form/div/dl[2]/dd/ul/li[3]/input


sleep(3)

