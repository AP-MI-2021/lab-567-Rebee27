from Domain.companie_aeriana import getPret, getNume


def sumaPreturilor(lista):
    '''
    afiseaza suma preturilor pentru fiecare nume
    param lista: lista de rezervari
    return: suma preturilor pentru fiecare nume
    '''

    rezultat = {}
    for rezervare in lista:
        pret = getPret(rezervare)
        nume = getNume(rezervare)
        if nume in rezultat:
            rezultat[nume] = rezultat[nume] + pret
        else:
            rezultat[nume] = pret

    return rezultat
