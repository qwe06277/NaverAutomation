from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import pyperclip
from login import *
def search():
    driver = webdriver.Chrome()
    elem = driver.find_element_by_id("query")
    elem.send_keys("아이폰7")    
    elem = driver.find_element_by_id("search_btn")
    elem.click()

if __name__ == "__main__":
    login()
    search()

