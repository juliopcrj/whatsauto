import sys
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


#[attempt 1]
#timeout = 10
#for c in contacts:
#    driver.get("https://web.whatsapp.com/send?phone=" + c + "&text="+ message)
#    element_present = EC.presence_of_element_located((By.CLASS_NAME, 'OTBsx'))
#    WebDriverWait(driver, timeout).until(element_present)
#    button = driver.find_element_by_xpath('//button[@class="_1E0Oz"]')
#    button.click()
    

#[attempt 2]
def mass_send(contacts, message, source):
    options = webdriver.ChromeOptions()
    options.add_argument("--user-data-dir=./User_Data"+source)
    driver = webdriver.Chrome(chrome_options=options)

    for c in contacts:
        driver.get("https://web.whatsapp.com/send?phone=" + c + "&text=" + message)
        try:
            time.sleep(10)
            button = driver.find_element_by_xpath('//button[@class="_1E0Oz"]')
            button.click()
            with open("day_log.txt", "a+") as f:
                f.write("Enviado para " + c + "\n")
            time.sleep(5)
        except:
            print("Error")

    driver.quit()


if __name__ == "__main__":
    if(len(sys.argv) != 3):
        print("Forneça os arquivos de contatos e mensagem.\nO uso correto do programa é \npython "+sys.argv[0] + " arquivo_contato arquivo_mensagem")
        sys.exit(0)
    contacts = open(sys.argv[1]).read()[:-1].split("\n")
    message = open(sys.argv[2]).read()[:-1]
    #source = sys.argv[3]

    mass_send(contacts, message,"")
