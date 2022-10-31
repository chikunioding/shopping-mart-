from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(r"C:\Users\Mayur\PycharmProjects\shopping mart\driver\chromedriver.exe")
url=r"https://www.jiomart.com/"

driver.get(url)

driver.find_element(By.ID,"rel_search_list_btn").click()
driver.find_element(By.NAME,"searchTerm").send_keys("earphones")
driver.find_element(By.XPATH,"//button[text()=' Search Now ']").click()
driver.implicitly_wait(10)
A=driver.find_element(By.XPATH,"//img[@alt='PunnkFunnk Mat21 Wired Earphone']")
A.click()

driver.find_element(By.XPATH,"//button[@title='ADD TO CART']").click()

driver.find_element(By.XPATH,"//a[@class='cart_text']").click()
B=driver.find_element(By.XPATH,"//img[@class='pro-img ng-star-inserted']")
B.is_displayed()


