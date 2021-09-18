from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
import time 

driver = webdriver.Chrome(executable_path="D:\Selenium_Driver\chromedriver_win32\\chromedriver.exe")

driver.maximize_window()

driver.get("https://web.whatsapp.com/")

time.sleep(5)

Grup = driver.find_element_by_xpath('//*[@id="pane-side"]/div[2]/div/div/div[3]/div/div').click()

Mesagge_area = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/div/div[1]/div[1]/button[2]/span').click()

time.sleep(2)
    
Sticker_base = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/div/div[1]/div[1]/button[4]').click()

time.sleep(2)

Sticker = driver.find_element_by_xpath('//*[@id="main"]/footer/div[2]/div/div[3]/div[1]/div/div[1]/div[2]/div/div[1]/div/span').click()

def Gonder(sayi):
    if sayi > 0:
        Gonder(sayi - 1)
        Sticker = driver.find_element_by_xpath('//*[@id="main"]/footer/div[2]/div/div[3]/div[1]/div/div[1]/div[2]/div/div[1]/div/span').click()
 
 
Gonder(60)

