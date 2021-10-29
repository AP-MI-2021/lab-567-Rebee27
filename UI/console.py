from Logic.CRUD import adaugaRezervare, stergeRezervare, modificaRezervare
from Domain.companie_aeriana import toStrig
from Logic.functionalitate2 import trecereCLasaSuperioara
from Logic.functionalitate3 import ieftinireRezervari
from Logic.functionalitate4 import pretMaxim
from Logic.functionalitate5 import ordonareDescrescatoare
from Logic.functionalitate6 import sumaPreturilor


def printMenu():
    print("1. Adaugare rezervare")
    print("2. Stergere rezervare")
    print("3. Modificare rezervare")
    print("4. Trecere la o clasa superioara")
    print("5. Ieftinire rezervari cu checkin-ul facut")
    print("6. Pretul maxim al fiecarei clase")
    print("7. Ordonare descrescatoare dupa pret")
    print("8. Suma prețurilor pentru fiecare nume.")
    print("a. Afisare rezervari")
    print("x. Iesire")


def uiAdaugaRezervare(lista):
    try:
        id = input("Dati id-ul: ")
        nume = input("Dati numele: ")
        clasa = input("Specificati clasa (economy/economy plus/business): ")
        pret = float(input("Dati pretul: "))
        checkin = (input("Specificati daca checkin-ul e facut sau nu: "))
        return adaugaRezervare(id, nume, clasa, pret, checkin, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiStergeRezervare(lista):
    try:
        id = input("Dati id-ul: ")
        return stergeRezervare(id, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def uiModificaRezervare(lista):
    try:
        id = input("Dati id-ul rezervarii de modificat: ")
        nume = input("Dati noul nume: ")
        clasa = input("Specificati noua clasa (economy/economy plus/business): ")
        pret = float(input("Dati noul pret: "))
        checkin = (input("Specificati daca checkin-ul e facut sau nu: "))
        return  modificaRezervare(id, nume, clasa, pret, checkin, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def showAll(lista):
    for rezervare in lista:
        print(toStrig(rezervare))


def uiClasaSuperioasa(lista):
    try:
        numeDat = input("Dati numele pentru care rezervarile se vor trece la o clasa superioara: ")
        return trecereCLasaSuperioara(numeDat, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def uiIeftinireRezervari(lista):
    try:
        procentajDat = input("Dati procentajul cu care se vor ieftini rezervarile cu checkin-ul facut: ")
        return ieftinireRezervari(procentajDat, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def uiPretMaxim(lista):
    rezultat = pretMaxim(lista)
    for clasa in rezultat:
        print("Pretul maxim pentru clasa ", clasa, "este: ", rezultat[clasa])


def uiOrdonareDescrescatoare(lista):
    return ordonareDescrescatoare(lista)


def uiSumaPreturilor(lista):
    rezultat = sumaPreturilor(lista)
    for nume in rezultat:
        print("Suma preturilor pentru numele ", nume, "este: ", rezultat[nume])


def runMenu(lista):
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")

        if optiune == "1":
            lista = uiAdaugaRezervare(lista)
        elif optiune == "2":
            lista = uiStergeRezervare(lista)
        elif optiune == "3":
            lista = uiModificaRezervare(lista)
        elif optiune == "4":
            lista = uiClasaSuperioasa(lista)
        elif optiune == "5":
            lista = uiIeftinireRezervari(lista)
        elif optiune == "6":
            uiPretMaxim(lista)
        elif optiune == "7":
            lista = uiOrdonareDescrescatoare(lista)
        elif optiune== "8":
            uiSumaPreturilor(lista)
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita. Reincercati! ")


