from Domain.companie_aeriana import *
from Logic.CRUD import *


def testAdaugaRezervare():
    lista = []
    lista = adaugaRezervare("1", "Popescu", "economy", 250, "da", lista)

    assert getId(getById("1", lista)) == "1"
    assert getNume(getById("1", lista)) == "Popescu"
    assert getClasa(getById("1", lista)) == "economy"
    assert getPret(getById("1", lista)) == 250
    assert getCheckin(getById("1", lista)) == "da"


def testStergeRezervare():
    lista = []
    lista = adaugaRezervare("1", "Popescu", "economy", 250, "da", lista)
    lista = adaugaRezervare("2", "Ionescu", "business", 400, "nu", lista)

    lista = stergeRezervare("1", lista)

    assert getNume(getById("2", lista)) is not None


def testModificaRezervare():
    lista = []
    lista = adaugaRezervare("1", "Popescu", "economy", 250, "da", lista)
    lista = adaugaRezervare("2", "Ionescu", "business", 400, "nu", lista)

    lista = modificaRezervare("2", "Popescu", "economy", 300, "nu", lista)

    assert getCheckin(getById("2", lista)) == "nu"
    assert getPret(getById("2", lista)) == 300


