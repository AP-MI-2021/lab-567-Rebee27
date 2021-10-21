from Domain.companie_aeriana import *


def trecereClasaSuperioara(stringNume, lista):
    '''
    trecere rezervarilor facute pe un nume dat la o clasa superioara
    ;param substringNume: string
    ;param lista: lista de rezervari
    return: lista cu rezervarile dupa modificarea claselor
    '''
    listaNoua = []

    for rezervare in lista:
        if getNume(rezervare) == stringNume and getClasa(rezervare) == "economy":
            rezervareNoua = creeazaRezervare(
                getId(rezervare),
                getNume(rezervare),
                "economy plus",
                getPret(rezervare),
                getCheckin(rezervare)
            )
            listaNoua.append(rezervareNoua)
        elif getNume(rezervare) == stringNume and getClasa(rezervare) == "economy plus":
            rezervareNoua = creeazaRezervare(
                getId(rezervare),
                getNume(rezervare),
                "business",
                getPret(rezervare),
                getCheckin(rezervare)
            )
            listaNoua.append(rezervareNoua)
        elif getNume(rezervare) == stringNume and getClasa(rezervare) == "business":
            listaNoua.append(rezervare)

    return listaNoua

