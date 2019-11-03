
##########################################################################
# 									 #
# 									 #
# 			Author : Vyshak Puthusseri			 #
# 			github: puthusseri				 #
# 									 #
##########################################################################

import time
import sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome('./chromedriver')
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)

nameOfFriend = input("Enter the name of the recipient inside a single quotes: ")
string = input("Enter the msg: ")
x_arg = '//span[contains(@title,' + nameOfFriend + ')]'
group_title = wait.until(EC.presence_of_element_located((
	By.XPATH, x_arg)))
group_title.click()
n = int(input("Enter the number of times to send the msg: "))
for i in range(n):
	message = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]
	message.send_keys(string)
	sendbutton = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
	sendbutton.click()
driver.close()

