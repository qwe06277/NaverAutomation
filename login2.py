from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import pyperclip


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(3)
driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com")
sleep(3)
pyperclip.copy('qwe06277')
driver.find_element_by_id("id").send_keys(Keys.CONTROL, 'v')
pyperclip.copy('yoongayoung1030!')
driver.find_element_by_id("pw").send_keys(Keys.CONTROL, 'v')
driver.find_element_by_id("log.login").click()
sleep(3)
driver.find_element_by_id("new.save").click()