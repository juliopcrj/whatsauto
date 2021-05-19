import sys, os
import selenium.webdriver as wd
from selenium.webdriver.common.keys import Keys
import time

def mass_send(driver, contacts, message):
    driver.get("https://web.whatsapp.com")
    time.sleep(25)
    search_field = driver.find_element_by_class_name("_2_1wd")

    for c in contacts:
        search_field.click()
        search_field.send_keys(Keys.CONTROL, 'a')
        search_field.send_keys(Keys.BACKSPACE)
        search_field.send_keys(c)
        time.sleep(2)
        try:
            search_field.send_keys(Keys.DOWN)
            search_field.send_keys(Keys.RETURN)
            box = driver.switch_to.active_element
            box.send_keys(message)
            box.send_keys(Keys.RETURN)
            with open("log_day.txt", "a+") as f:
                f.write("Enviou para " + c + "\n")
            time.sleep(2)
        except Exception:
            with open("log_error.txt", "a+") as f:
                f.write("Erro enviando para " + c +"\n")
            time.sleep(2)


if __name__ == "__main__":
    if(len(sys.argv) != 3):
        print("Uso correto:\npython "+sys.argv[0] + " arquivo_contato arquivo_mensagem\n")
        sys.exit(0)

    options = wd.ChromeOptions()
    options.add_argument("--user-data-dir="+ os.path.join(".","User_Data"))
    driver = wd.Chrome(options=options)
    contacts = open(sys.argv[1]).read().split("\n")
    contacts = [c for c in contacts if c != ""] #gambiarra para remover linhas vazias.
    message = open(sys.argv[2], encoding="utf-8").read()
    sys.exit(mass_send(driver, contacts, message))

