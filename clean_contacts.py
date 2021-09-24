#!/usr/bin/python3

from os.path import abspath, exists, sep
from shutil import copyfile


def main():
    if not exists(abspath("backup.txt")):
        copyfile(abspath("contatos.txt"), abspath("." + sep + "backup.txt") )

    all_contacts = open("backup.txt").read()[:-1].split("\n")
    try:
        ans_contacts = open("responderam.txt").read()[:-1].split("\n")
    except FileNotFoundError:
        print("Arquivo 'responderam.txt' faltando, por favor coloque-o nesta pasta e tente novamente")
        exit(1)

    #codigo,contato
    contacts_dict = [i.split(",") for i in open("dicionario.csv").read()[:-1].split("\n")]

    for i in contacts_dict:
        if i[0] in ans_contacts:
            try:
                all_contacts.remove(i[1])
            except ValueError:
                # já foi removido previamente, ignore.
                pass

    with open("contatos.txt", "w") as file:
        for i in all_contacts:
            file.write(i + "\n")


if __name__ == "__main__":
    main()
