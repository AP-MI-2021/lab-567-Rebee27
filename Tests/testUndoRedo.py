from Domain.companie_aeriana import getId
from Logic.CRUD import adaugaRezervare, stergeRezervare


def testUndoRedo():
    lista = []                                                                                          #punctul1
    undoList = []
    redoList = []

    lista = adaugaRezervare("1", "obiect1", "economy", 340, "da", lista)                                #punctul2
    undoList.append([
        lambda: stergeRezervare("1", lista),
        lambda: adaugaRezervare("1", "obiect1", "economy", 340, "da", lista)
    ])
    redoList.clear()
    assert len(lista) == 1
    assert getId(lista[0]) == "1"

    lista = adaugaRezervare("2", "obiect2", "economy plus", 500, "nu", lista)                           #punctul3
    undoList.append([
        lambda: stergeRezervare("2", lista),
        lambda: adaugaRezervare("2", "obiect2", "economy plus", 500, "nu", lista)
    ])
    redoList.clear()
    assert len(lista) == 2
    assert getId(lista[0]) == "1"
    assert getId(lista[1]) == "2"

    lista = adaugaRezervare("3", "obiect3", "business", 200, "da", lista)                               #punctul4
    undoList.append([
        lambda: stergeRezervare("3", lista),
        lambda: adaugaRezervare("3", "obiect3", "business", 200, "da", lista)
    ])
    redoList.clear()
    assert len(lista) == 3
    assert getId(lista[2]) == "3"

    operations = undoList.pop()                                                                         #punctul5
    redoList.append(operations)
    lista = operations[0]()
    assert len(lista) == 2
    assert getId(lista[1]) == "2"

    operations = undoList.pop()                                                                         #punctul6
    redoList.append(operations)
    lista = operations[0]()
    assert len(lista) == 1
    assert getId(lista[0]) == "1"

    operations = undoList.pop()                                                                         #punctul7
    redoList.append(operations)
    lista = operations[0]()
    assert len(lista) == 0

    if len(undoList) > 0:                                                                               #punctul8
        operations = undoList.pop()
        redoList.append(operations)
        lista = operations[0]()
    #print : nu se poate face undo


    lista = adaugaRezervare("1", "obiect1", "economy", 340, "da", lista)                                #punctul9
    undoList.append([
        lambda: stergeRezervare("1", lista),
        lambda: adaugaRezervare("1", "obiect1", "economy", 340, "da", lista)
    ])
    redoList.clear()
    lista = adaugaRezervare("2", "obiect2", "economy plus", 500, "nu", lista)
    undoList.append([
        lambda: stergeRezervare("2", lista),
        lambda: adaugaRezervare("2", "obiect2", "economy plus", 500, "nu", lista)
    ])
    redoList.clear()
    lista = adaugaRezervare("3", "obiect3", "business", 200, "da", lista)
    undoList.append([
        lambda: stergeRezervare("3", lista),
        lambda: adaugaRezervare("3", "obiect3", "business", 200, "da", lista)
    ])
    redoList.clear()

    if len(redoList) > 0:                                                                              #punctul10
        operations = redoList.pop()
        undoList.append(operations)
        lista = operations[1]()
    #print : nu se poate face redo

    operations = undoList.pop()                                                                        #punctul11
    redoList.append(operations)
    lista = operations[0]()
    assert len(lista) == 2
    assert getId(lista[1]) == "2"

    operations = undoList.pop()
    redoList.append(operations)
    lista = operations[0]()
    assert len(lista) == 1
    assert getId(lista[0]) == "1"

    operations = redoList.pop()                                                                        #punctul12
    undoList.append(operations)
    lista = operations[1]()
    assert len(lista) == 2
    assert getId(lista[1]) == "2"

    operations = redoList.pop()                                                                        #punctul13
    undoList.append(operations)
    lista = operations[1]()
    assert len(lista) == 3
    assert getId(lista[1]) == "2"
    assert getId(lista[2]) == "3"

    operations = undoList.pop()                                                                        #punctul14
    redoList.append(operations)
    lista = operations[0]()
    assert len(lista) == 2
    assert getId(lista[1]) == "2"

    operations = undoList.pop()
    redoList.append(operations)
    lista = operations[0]()
    assert len(lista) == 1
    assert getId(lista[0]) == "1"

    lista = adaugaRezervare("4", "obiect4", "economy", 340, "da", lista)                              #punctul15
    undoList.append([
        lambda: stergeRezervare("4", lista),
        lambda: adaugaRezervare("4", "obiect4", "economy", 340, "da", lista)
    ])
    redoList.clear()
    assert len(lista) == 2
    assert getId(lista[0]) == "1"
    assert getId(lista[1]) == "4"

    if len(redoList) > 0:                                                                             #punctul16
        operations = redoList.pop()
        undoList.append(operations)
        lista = operations[1]()
    #print : nu se poate face redo
    assert len(lista) == 2
    assert getId(lista[0]) == "1"
    assert getId(lista[1]) == "4"

    operations = undoList.pop()                                                                       #punctul17
    redoList.append(operations)
    lista = operations[0]()
    assert len(lista) == 1
    assert getId(lista[0]) == "1"

    operations = undoList.pop()                                                                       #punctul18
    redoList.append(operations)
    lista = operations[0]()
    assert len(lista) == 0

    if len(redoList) > 0:                                                                             #punctul19
        operations = redoList.pop()
        undoList.append(operations)
        lista = operations[1]()
    if len(redoList) > 0:
        operations = redoList.pop()
        undoList.append(operations)
        lista = operations[1]()
    assert len(lista) == 2
    assert getId(lista[0]) == "1"
    assert getId(lista[1]) == "4"

    if len(redoList) > 0:                                                                             #punctul20
        operations = redoList.pop()
        undoList.append(operations)
        lista = operations[1]()
    #print : nu se poate face redo
    assert len(lista) == 2
    assert getId(lista[0]) == "1"
    assert getId(lista[1]) == "4"














