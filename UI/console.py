from Logic.CRUD import adaugaRezervare, stergeRezervare, modificaRezervare
from Domain.companie_aeriana import toStrig
from Logic.functionalitate2 import trecereCLasaSuperioara
from Logic.functionalitate4 import pretMaxim


def printMenu():
    print("1. Adaugare rezervare")
    print("2. Stergere rezervare")
    print("3. Modificare rezervare")
    print("4. Trecere la o clasa superioara")
    print("5. Pretul maxim al fiecarei clase")
    print("a. Afisare rezervari")
    print("x. Iesire")


def uiAdaugaRezervare(lista):
    id = input("Dati id-ul: ")
    nume = input("Dati numele: ")
    clasa = input("Specificati clasa (economy/economy plus/business): ")
    pret = float(input("Dati pretul: "))
    checkin = (input("Specificati daca checkin-ul e facut sau nu: "))
    return adaugaRezervare(id, nume, clasa, pret, checkin, lista)


def uiStergeRezervare(lista):
    id = input("Dati id-ul: ")
    return stergeRezervare(id, lista)


def uiModificaRezervare(lista):
    id = input("Dati id-ul rezervarii de modificat: ")
    nume = input("Dati noul nume: ")
    clasa = input("Specificati noua clasa (economy/economy plus/business): ")
    pret = float(input("Dati noul pret: "))
    checkin = (input("Specificati daca checkin-ul e facut sau nu: "))
    return  modificaRezervare(id, nume, clasa, pret, checkin, lista)


def showAll(lista):
    for rezervare in lista:
        print(toStrig(rezervare))


def uiClasaSuperioasa(lista):
    numeDat = input("Dati numele pentru care rezervarile se vor trece la o clasa superioara: ")
    return trecereCLasaSuperioara(numeDat, lista)


def uiPretMaxim(lista):
    return pretMaxim(lista)


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
            print("Pretul maxim pentru clasele economy, economy plus respectiv business sunt: ", uiPretMaxim(lista))
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita. Reincercati! ")


