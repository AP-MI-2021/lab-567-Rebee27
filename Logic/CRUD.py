from Domain.companie_aeriana import creeazaRezervare, getId


def adaugaRezervare(id, nume, clasa, pret, checkin, lista):
    '''
    adauga o rezervare intr-o lista
    ;param id: string
    ;param nume: string
    ;param clasa: string
    ;param pret: float
    ;param checkin: bool
    ;param lista: lista de rezervari
    return: o lista continand elementele vechi,cat si noua rezervare
    '''
    rezervare = creeazaRezervare(id, nume, clasa, pret, checkin)
    return lista + [rezervare]


def getById(id, lista):
    '''
    da rezervarea cu id-ul dat dintr-o lista
    ;param id: string
    ;param lista: lista de rezervari
    return: rezervarea cu id-ul dat din lista, sau None daca aceasta nu exista
    '''
    for rezervare in lista:
        if getId(rezervare) == id:
            return rezervare
    return None


def stergeRezervare(id, lista):
    '''
    sterge o rezervare identificata cu id dintr-o lista
    ;param id: string
    ;param lista: lista de rezervari
    return: lista dupa stergerea unei rezervari
    '''
    return [rezervare for rezervare in lista if getId(rezervare) != id]


def modificaRezervare(id, nume, clasa, pret, checkin, lista):
    '''
    modifica o rezervare dupa id
    ;param id: string
    ;param nume: string
    ;param clasa: string
    ;param pret: float
    ;param checkin: bool
    ;param lista: lista de rezervari
    return: lista cu rezervarea identificata prin id modificata
    '''
    listaNoua = []
    for rezervare in lista:
        if getId(rezervare) == id:
            rezervareNoua = creeazaRezervare(id, nume, clasa, pret, checkin)
            listaNoua.append(rezervareNoua)
        else:
            listaNoua.append(rezervare)
    return listaNoua
