from Domain.companie_aeriana import *


def ieftinireRezervari(procentajDat, lista):
    '''
    ieftinirea tuturor rezervarilor care au checkin-ul facut cu un procentaj dat de la tastatura
    param procentajDat: float
    param lista: lista de rezervari
    return: lista de rezervari dupa modificarile facute
    '''

    listaNoua = []

    for rezervare in lista:
        if getCheckin(rezervare) == "da":
            rezervareNoua = creeazaRezervare(
                getId(rezervare),
                getNume(rezervare),
                getClasa(rezervare),
                getPret(rezervare) - int((procentajDat / 100) * getPret(rezervare)),
                getCheckin(rezervare)
            )
            listaNoua.append(rezervareNoua)
        else:
            listaNoua.append(rezervare)

    return listaNoua
