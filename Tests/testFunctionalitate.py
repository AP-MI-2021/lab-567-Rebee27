from Domain.companie_aeriana import getClasa
from Logic.CRUD import adaugaRezervare, getById
from Logic.functionalitate import trecereCLasaSuperioara


def testTrecereClasaSuperioasa():
    lista = []
    lista = adaugaRezervare("1", "Popescu", "economy", 250, "da", lista)
    lista = adaugaRezervare("2", "Ionescu", "business", 400, "nu", lista)
    lista = adaugaRezervare("3", "Popescu", "economy plus", 250, "da", lista)
    lista = adaugaRezervare("4", "Popescu", "business", 400, "nu", lista)

    lista = trecereCLasaSuperioara("popescu", lista)

    assert getClasa(getById("1", lista)) == "economy plus"
    assert getClasa(getById("2", lista)) == "business"
    assert getClasa(getById("3", lista)) == "business"
