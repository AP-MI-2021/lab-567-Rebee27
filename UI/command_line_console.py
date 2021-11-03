from Logic.CRUD import adaugaRezervare, stergeRezervare
from Domain.companie_aeriana import toStrig


def help():
    print("""
    help -> arata acest meniu
    add,<id>,<titlu>,<gen>,<pret>,<reducere> -> adauga o vanzare
    remove,<id> -> sterge o vanzare
    showall -> arata toate vanzarile
    exit -> inchide programul
    """)

def add(rezervari, listaParametrii):
    id = listaParametrii[1]
    nume = listaParametrii[2]
    clasa = listaParametrii[3]
    pret = listaParametrii[4]
    checkin = listaParametrii[5]

    return adaugaRezervare(id, nume, clasa, pret, checkin, rezervari)

def delete(rezervari, listaParametrii):
    id = listaParametrii[1]

    return stergeRezervare(id, rezervari)

def showAll(rezervari):
    for rezervare in rezervari:
        print(toStrig(rezervare))

def comanda(rezervari):
    exit = False
    while exit == False:
        print("Introduceti comanda/comenzile separate prin ';' :")
        comenzi_introduse = input()

        comenzi = comenzi_introduse.split(";")
        for comanda in comenzi:
            listaParametrii = comanda.split(",")

            if listaParametrii[0] == "help":
                help()
            elif listaParametrii[0] == "add":
                rezervari = add(rezervari, listaParametrii)
            elif listaParametrii[0] == "showall":
                showAll(rezervari)
            elif listaParametrii[0] == "exit":
                exit = True


