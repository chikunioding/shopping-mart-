from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(r"C:\Users\Mayur\PycharmProjects\shopping mart\driver\chromedriver.exe")
driver.get(r"https://www.amazon.in/")

time.sleep(2)

print(driver.title)

driver.quit()