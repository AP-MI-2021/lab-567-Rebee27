from Logic.CRUD import adaugaRezervare
from Tests.testAll import runAllTests
from UI.console import runMenu


def main():
    runAllTests()
    lista = []
    lista = adaugaRezervare("1", "Popescu", "economy", 250, "da", lista)
    lista = adaugaRezervare("2", "Ionescu", "business", 400, "nu", lista)
    lista = adaugaRezervare("3", "Popescu", "economy plus", 250, "da", lista)
    lista = adaugaRezervare("4", "Popescu", "business", 400, "nu", lista)
    runMenu(lista)

main()