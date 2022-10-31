from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(r"C:\Users\Mayur\PycharmProjects\shopping mart\driver\chromedriver.exe")
url=r"http://122.166.192.191:9003/"

Z=driver.get(url)
M=driver.title
print(M)

if M=="Lara Classified - Qspiders all in one":
    print("title is matched")
else:
    print("title not matched")

driver.close()

