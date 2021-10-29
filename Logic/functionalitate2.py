from Domain.companie_aeriana import *


def trecereCLasaSuperioara(numeDat, lista):
    '''
    trecerea rezervarilor facute pe un nume dat la o clasa superioara
    ;param substringNume: string
    ;param lista: lista de rezervari
    return: lista cu rezervari dupa modificarea claselor
    '''
    listaNoua = []

    for rezervare in lista:
        if numeDat is not getNume(rezervare):
            raise ValueError("Nu exista o rezervare cu numele dat")
        if getNume(rezervare) == numeDat and getClasa(rezervare) == "economy":
            rezervareNoua = creeazaRezervare(
                getId(rezervare),
                getNume(rezervare),
                "economy plus",
                getPret(rezervare),
                getCheckin(rezervare)
            )
            listaNoua.append(rezervareNoua)
        elif getNume(rezervare) == numeDat and getClasa(rezervare) == "economy plus":
            rezervareNoua = creeazaRezervare(
                getId(rezervare),
                getNume(rezervare),
                "business",
                getPret(rezervare),
                getCheckin(rezervare)
            )
            listaNoua.append(rezervareNoua)
        elif getClasa(rezervare) == "business":
            listaNoua.append(rezervare)
        else:
            listaNoua.append(rezervare)

    return listaNoua



