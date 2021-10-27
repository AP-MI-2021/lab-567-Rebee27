from Domain.companie_aeriana import getPret
from Logic.CRUD import adaugaRezervare, getById
from Logic.functionalitate3 import ieftinireRezervari


def testTrecereClasaSuperioasa():
    lista = []
    lista = adaugaRezervare("1", "Popescu", "economy", 250, "da", lista)
    lista = adaugaRezervare("2", "Ionescu", "business", 400, "nu", lista)
    lista = adaugaRezervare("3", "Popescu", "economy plus", 100, "da", lista)
    lista = adaugaRezervare("4", "Popescu", "business", 400, "nu", lista)

    lista = ieftinireRezervari(10, lista)

    assert getPret(getById("1", lista)) == 225
    assert getPret(getById("2", lista)) == 400
    assert getPret(getById("3", lista)) == 90