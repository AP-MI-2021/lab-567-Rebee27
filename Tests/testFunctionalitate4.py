from Logic.CRUD import adaugaRezervare
from Logic.functionalitate4 import pretMaxim


def testPretMaxim():
    lista = []
    lista = adaugaRezervare("1", "Popescu", "economy", 50, "da", lista)
    lista = adaugaRezervare("2", "Ionescu", "business", 400, "nu", lista)
    lista = adaugaRezervare("3", "Popescu", "economy plus", 250, "da", lista)
    lista = adaugaRezervare("4", "Popescu", "business", 350, "nu", lista)
    lista = adaugaRezervare("2", "Ionescu", "economy", 100, "nu", lista)

    rezultat = pretMaxim(lista)

    assert len(rezultat) == 3
    assert rezultat["economy"] == 100
    assert rezultat["economy plus"] == 250
    assert rezultat["business"] == 400