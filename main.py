from Logic.CRUD import adaugaRezervare
from Tests.testAll import runAllTests
from UI.command_line_console import comanda
from UI.console import runMenu


def main():
    runAllTests()
    lista = []
    lista = adaugaRezervare("1", "Popescu", "economy", 50, "da", lista)
    lista = adaugaRezervare("2", "Ionescu", "business", 400, "nu", lista)
    lista = adaugaRezervare("3", "Popescu", "economy plus", 250, "da", lista)
    lista = adaugaRezervare("4", "Popescu", "business", 350, "nu", lista)

    raspuns = int(input("Doriti sa utilizati meniul 1 sau meniul 2? "))
    if raspuns == 1:
        runMenu(lista)
    elif raspuns == 2:
        comanda(lista)
    else:
        print("Valoare gresita. Reincercati!")

main()