from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.chrome.options import Options
import time
#import pandas as pd



PATH = "C:/Users/shafe/Desktop/my work/chromedriver.exe"
url = "https://web.whatsapp.com"

driver = webdriver.Chrome(PATH)
driver.get(url)
msg = "Hi..."
# time.sleep(25)
no = [919526050007,918089281200]

no = list(map(int, no))
num = len(no)

WebDriverWait(driver, 120).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[3]/div/div[1]")))

# for i in range(0,num):
#     elm = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[1]')
#     driver.execute_script(f"arguments['0'].innerHTML = '<a href=\"https://api.whatsapp.com/send?phone={no[i]}id=\"contact{str(i+1)}>{str(i+1)}</a>';", elm)

#     msgele = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/div[1]/a")
#     msgele.click()
#     time.sleep(1)
#     focus = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
#     focus.send_keys(msg)
#     focus.send_keys(Keys.ENTER)

#     print('done')    


file_path = "C:/Users/shafe/Desktop/test.jpg"#file path

from time import sleep#sending image to whatsapp

# For sending message
for i in range(0,num):
    elm = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[1]')
    driver.execute_script(f"arguments['0'].innerHTML = '<a href=\"https://api.whatsapp.com/send?phone={no[i]}id=\"contact{str(i+1)}>{str(i+1)}</a>';", elm)
    msgele = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/div[1]/a")
    msgele.click()
    time.sleep(2)

    attachment_section = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[1]/div[2]/div/div')
    attachment_section.click()
    image_box = driver.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
    image_box.send_keys(file_path)
    WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div'))).click()