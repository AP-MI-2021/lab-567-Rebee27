from Domain.companie_aeriana import toStrig
from Logic.CRUD import adaugaRezervare, stergeRezervare, modificaRezervare


def help():
    print("""
    help                                        -> arata acest meniue
    add,<id>,<titlu>,<gen>,<pret>,<reducere>    -> adauga o rezervare
    delete,<id>                                 -> sterge o rezervare
    modify,<id>,<titlu>,<gen>,<pret>,<reducere> -> modifica o rezervare
    showall                                     -> arata toate rezervarile
    exit                                        -> inchide programul
    """)


def add(rezervareNoua, lista):
    try:
        id = rezervareNoua[1]
        nume = rezervareNoua[2]
        clasa = rezervareNoua[3]
        pret = float(rezervareNoua[4])
        checkin = rezervareNoua[5]
        return adaugaRezervare(id, nume, clasa, pret, checkin, lista)
    except ValueError as ve:
        print("Eroare: ", ve)
    return lista


def delete(rezervareDeSters, lista):
    try:
        id = rezervareDeSters[1]
        lista = stergeRezervare(id, lista)
    except ValueError as ve:
        print("Eroare: ", ve)
    return lista


def modify(rezervareDeModificat, lista):
    try:
        id = rezervareDeModificat[1]
        nume = rezervareDeModificat[2]
        clasa = rezervareDeModificat[3]
        pret = rezervareDeModificat[4]
        checkin = rezervareDeModificat[5]
        lista = modificaRezervare(id, nume, clasa, pret, checkin, lista)
    except ValueError as ve:
        print("Eroare: ", ve)
    return lista

def showAll(lista):
    for rezervare in lista:
        print(toStrig(rezervare))


def comanda(lista):
    lista = []
    exit = False
    try:
        while exit == False:
            comenzi = input("Introduceti comanda/comenzile separate prin ';' :")
            comenzi = comenzi.split(";")

            for comanda in comenzi:
                comanda = comanda.split(",")
                rezervari = []

                for detalii in comanda:
                    rezervari.append(detalii)
                if rezervari[0] == "help":
                    help()
                elif rezervari[0] == "add":
                    lista = add(rezervari, lista)
                elif rezervari[0] == "delete":
                    lista = delete(rezervari, lista)
                elif rezervari[0] == "modify":
                    lista = modify(rezervari, lista)
                elif rezervari[0] == "showall":
                    showAll(lista)
                elif rezervari[0] == "exit":
                    exit = True
                else:
                    print("Comanda gresita. Reincercati!")
    except ValueError as ve:
        print("Eroare!", ve)
