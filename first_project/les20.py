from time import sleep

from selenium import webdriver

URL = 'http://www.google.com'

options: webdriver.ChromeOptions = webdriver.ChromeOptions()

# options.add_argument("--window-size=1920,1080")  # window size
options.add_argument("--start-maximized")  # развернуть на весь экран
# options.add_argument("--disable-gpu")  # disable GPU
# options.add_argument("--headless=new")  # отключение отображения браузера


driver = webdriver.Chrome(options=options)
driver.get(URL)
sleep(5)
