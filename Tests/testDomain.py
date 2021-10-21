from Domain.companie_aeriana import *


def testRezervare():
    rezervare = creeazaRezervare("1", "Popescu", "economy", 250, "da")

    assert getId(rezervare) == "1"
    assert getNume(rezervare) == "Popescu"
    assert getClasa(rezervare) == "economy"
    assert getPret(rezervare) == 250
    assert getCheckin(rezervare) == "da"