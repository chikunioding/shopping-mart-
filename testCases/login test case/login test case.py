from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(r"C:\Users\Mayur\PycharmProjects\shopping mart\driver\chromedriver.exe")
url=r"http://122.166.192.191:9003/"

Z=driver.get(url)
A=driver.find_element(By.XPATH,"//a[text()='Login']")
A.click()
B=driver.find_element(By.ID,"email")
B.send_keys("majnupro@gmail.com")
C=driver.find_element(By.ID,"password")
C.send_keys("Majnu@1234")
D=driver.find_element(By.XPATH,"//button[@id='loginBtn']")
D.click()
M=driver.title
driver.find_element(By.XPATH,"//input[@id='phone']").send_keys("8754612852")
driver.find_element(By.XPATH,"//button[@class='btn btn-primary']").click()
T=driver.find_element(By.XPATH,"//div[@class='alert alert-success']/button")
T.is_displayed()


if M=="My account":
    print(M)
    print("login successfully")

else:
    print("unable to login")
