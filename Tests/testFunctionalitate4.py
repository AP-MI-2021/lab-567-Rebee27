from Logic.CRUD import adaugaRezervare
from Logic.functionalitate4 import pretMaxim


def testPretMaxim():
    lista = []
    lista = adaugaRezervare("1", "Popescu", "economy", 250, "da", lista)
    lista = adaugaRezervare("2", "Ionescu", "business", 300, "nu", lista)
    lista = adaugaRezervare("3", "Popescu", "economy plus", 175, "da", lista)
    lista = adaugaRezervare("4", "Popescu", "business", 400, "nu", lista)
    lista = adaugaRezervare("5", "Popescu", "economy", 75, "da", lista)
    lista = adaugaRezervare("6", "Ionescu", "business", 125, "nu", lista)
    lista = adaugaRezervare("7", "Popescu", "economy plus", 308, "da", lista)
    lista = adaugaRezervare("8", "Popescu", "business", 29, "nu", lista)

    assert pretMaxim(lista) == [250, 308, 400]