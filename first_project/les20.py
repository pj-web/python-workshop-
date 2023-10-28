from time import sleep

from selenium import webdriver

URL = 'http://www.google.com'

options = webdriver.ChromeOptions()

options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)
driver.get(URL)
sleep(5)
