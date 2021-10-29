from Logic.CRUD import adaugaRezervare
from Logic.functionalitate6 import sumaPreturilor


def testSumaPreturilor():
    lista = []
    lista = adaugaRezervare("1", "Popescu", "economy", 250, "da", lista)
    lista = adaugaRezervare("2", "Ionescu", "business", 300, "nu", lista)
    lista = adaugaRezervare("3", "Popescu", "economy plus", 150, "da", lista)
    lista = adaugaRezervare("4", "Ionescu", "business", 400, "nu", lista)

    rezultat = sumaPreturilor(lista)

    assert len(rezultat) == 2
    assert rezultat["Popescu"] == 400
    assert rezultat["Ionescu"] == 700
