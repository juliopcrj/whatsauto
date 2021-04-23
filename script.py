from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir=./User_Data")
driver = webdriver.Chrome(chrome_options=options)

contacts = open("contacts.csv").read()[:-1].split("\n")
message = open("message.csv").read()[:-1].split("\n")[0]

timeout = 10

#[attempt 1]
for c in contacts:
    driver.get("https://web.whatsapp.com/send?phone=" + c + "&text="+ message)
    try:
        element_present = EC.presence_of_element_located((By.CLASS_NAME, 'OTBsx'))
        WebDriverWait(driver, timeout).until(element_present)
        button = driver.find_element_by_xpath('//button[@class="_1E0Oz"]')
        button.click()
        continue
    except:
        print("Page took too long to load")


#[attempt 2]

for c in contacts:
    driver.get("https://web.whatsapp.com/send?phone=" + c + "&text=" + message)
    try:
        time.sleep(10)
        button = driver.find_element_by_xpath('//button[@class="_1E0Oz"]')
        button.click()
    except:
        print("Error")
