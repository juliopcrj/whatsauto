#!/usr/bin/python3

import sys, os
import platform
import selenium.webdriver as wd
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import WebDriverException, NoSuchElementException
from datetime import datetime
from cryptography.fernet import Fernet

class WhatsAuto:

    def __init__(self):
        self.key = b'1Yf0fakZVOCMY7LoG6r_B6rNLBK3Y02kRAYnmQZNd3Q='
        pass

    def mass_send(self, driver, contacts, message):
        driver.get("https://web.whatsapp.com")
        time.sleep(25) #tempo para parear o telefone com o whatsapp web
        try:
            search_field = driver.find_element_by_class_name("_13NKt") #o campo de pesquisa de contato
            message = message.split("\n")

            for c in contacts:
                search_field.click() #seleciona o campo de busca, e apaga tudo o que tem dentro dele
                search_field.send_keys(Keys.CONTROL, 'a')
                search_field.send_keys(Keys.BACKSPACE)
                search_field.send_keys(c) #escreve o nome do contato no campo de busca
                time.sleep(2) #tempo de espera para o whatsapp web encontrar o contato
                try:
                    search_field.send_keys(Keys.DOWN) #envia a tecla DOWN para selecionar o primeiro contato encontrado na lista 
                    _temp = driver.switch_to.active_element #_temp é o elemento de item na lista de contato

                    if c.lower() not in _temp.text[:len(c)].lower() or _temp == search_field:
                        raise Exception #contato não está salvo no dispositivo ou não possui whatsapp

                    search_field.send_keys(Keys.RETURN) #caso o contato esteja na lista e não gerou exceção, aperta enter para escolher o contato
                    box = driver.switch_to.active_element #box é o campo de mensagem
                    for line in message:
                        if line == "":
                            box.send_keys(Keys.SHIFT, Keys.RETURN) #caso a linha seja vazia, insere uma linha vazia
                        else:
                            box.send_keys(line)
                            box.send_keys(Keys.SHIFT,Keys.RETURN) #caso contrário, insere a linha e uma quebra de linha
                    box.send_keys(Keys.RETURN) #aperta enter para enviar a mensagem
                    with open("log_sent.txt", "a+") as f:
                        f.write(datetime.now().strftime("%Y/%m/%d-%H:%M:%S") + " - Enviou para " + c + "\n") #salva em um log para saber para quais contatos a mensagem foi enviada
                    time.sleep(3) #aguarda enviar a mensagem
                except (WebDriverException, Exception):
                    with open("log_error.txt", "a+") as f:
                        f.write(datetime.now().strftime("%Y/%m/%d-%H:%M:%S") + " - Erro enviando para " + c +"\n") #caso tenha acontecido erro, salva quais contatos não receberam
                    time.sleep(1)
        except NoSuchElementException: #não leu o QR code a tempo, ou não carregou o whatsapp web a tempo
            print("WhatsApp web não carregou no tempo determinado, tente novamente")
        driver.close()


    def run(self):
        try:
            product_key = open("key.txt").read().encode("UTF8")
        except FileNotFoundError:
            print("Você não tem uma chave de uso, por favor entre em contato para obter uma.\n")
            exit(0)
        datestr = Fernet(self.key).decrypt(product_key).decode("UTF8")
        last_date = datetime.strptime(datestr, "%Y/%m/%d")
        if datetime.today() > last_date:
            print("Sua chave expirou. Por favor, entre em contato para obter uma chave nova.\n")
            exit(0)

        _os = platform.system()

        if _os != "Windows":
            if(len(sys.argv) != 3):
                print("Uso correto:\npython "+sys.argv[0] + " arquivo_contato arquivo_mensagem\n")
                sys.exit(0)

        if(_os != "Windows"):
            options = wd.ChromeOptions()
            options.add_argument("--user-data-dir="+ os.path.join(".","User_Data"))
            driver = wd.Chrome(options=options)
            contacts = open(sys.argv[1]).read().split("\n")
            message = open(sys.argv[2], encoding="utf-8").read()

        else:
            driver = wd.Chrome(executable_path="chromedriver.exe")
            contacts = open("contatos.txt").read().split("\n")
            message = open("mensagem.txt", encoding="utf-8").read()

        contacts = [c for c in contacts if c != ""] #gambiarra para remover linhas vazias.
        sys.exit(self.mass_send(driver, contacts, message))

