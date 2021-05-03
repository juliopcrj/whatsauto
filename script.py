import sys
import selenium.webdriver as wd
from selenium.webdriver.common.keys import Keys
import time

def mass_send(driver, contacts, message):
    driver.get("https://web.whatsapp.com")
    time.sleep(15)
    search_field = driver.find_element_by_class("_2_1wd")

    for c in contacts:
        search_field.click()
        search_field.send_keys(c)
        time.sleep(2)
        search_field.send_keys(Keys.DOWN)
        search_field.send_keys(Keys.RETURN)
        box = driver.switch_to.active_element
        box.send_keys(message)
        box.send_keys(Keys.RETURN)
        time.sleep(2)


if __name__ == "__main__":
    if(len(sys.argv) != 3):
        print("Uso correto:\npython "+sys.argv[0] + " arquivo_contato arquivo_mensagem\n")
        sys.exit(0)

    options = wd.ChromeOptions()
    options.add_argument("--user-data-dir=./User_Data")
    driver = wd.Chrome(options=options)
    contacts = open(sys.argv[1]).read()[:-1].split("\n")
    message = open(sys.argv[2]).read()
    sys.exit(mass_send(driver, contacts, message))

