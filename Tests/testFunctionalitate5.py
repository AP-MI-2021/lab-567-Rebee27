from Domain.companie_aeriana import getId
from Logic.CRUD import adaugaRezervare
from Logic.functionalitate5 import ordonareDescrescatoare


def testOrdonareDescrescatoare():
    lista = []
    lista = adaugaRezervare("1", "Popescu", "economy", 250, "da", lista)
    lista = adaugaRezervare("2", "Ionescu", "business", 300, "nu", lista)
    lista = adaugaRezervare("3", "Popescu", "economy plus", 175, "da", lista)
    lista = adaugaRezervare("4", "Popescu", "business", 400, "nu", lista)
    lista = adaugaRezervare("5", "Popescu", "economy", 75, "da", lista)
    lista = adaugaRezervare("6", "Ionescu", "business", 125, "nu", lista)
    lista = adaugaRezervare("7", "Popescu", "economy plus", 308, "da", lista)
    lista = adaugaRezervare("8", "Popescu", "business", 29, "nu", lista)

    lista = ordonareDescrescatoare(lista)

    assert getId(lista[0]) == "4"
    assert getId(lista[1]) == "7"
    assert getId(lista[2]) == "2"
    assert getId(lista[3]) == "1"


