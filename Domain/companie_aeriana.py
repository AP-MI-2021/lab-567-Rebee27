def creeazaRezervare(id, nume, clasa, pret, checkin):
    '''
    creeaza un dictionar ce reprezinta o rezervare pentru zbor
    ;param id: string
    ;param nume: string
    ;param clasa: string
    ;param pret: float
    ;param checkin: string
    return: un dictionar ce contine o rezervare
    '''
    return {
        "id": id,
        "nume": nume,
        "pret": pret,
        "clasa": clasa,
        "checkin": checkin
    }

def getId(rezervare):
    '''
    da id-ul unei rezervari
    ;param rezervare: dictionar ce contine o rezervare
    return: id-ul rezervarii
    '''
    return rezervare["id"]


def getNume(rezervare):
    '''
    da numele unei rezervari
    ;param rezervare: dictionar ce contine o rezervare
    return: nuemle rezervarii
    '''
    return rezervare["nume"]


def getClasa(rezervare):
    '''
    da clasa unei rezervari
    ;param rezervare: dictionar ce contine o rezervare
    return: clasa rezervarii
    '''
    return rezervare["clasa"]


def getPret(rezervare):
    '''
    da pretul unei rezervari
    ;param rezervare: dictionar ce contine o rezervare
    return: pretul rezervarii
    '''
    return rezervare["pret"]


def getCheckin(rezervare):
    '''
    da valoarea checkin-ului unei rezervari(da sau nu)
    ;param rezervare: dictionar ce contine o rezervare
    return: checkin-ul rezervarii
    '''
    return rezervare["checkin"]

def toStrig(rezervare):
    return "Id: {}, Nume: {}, Clasa: {}, Pret: {}, Checkin: {}".format(
        getId(rezervare),
        getNume(rezervare),
        getClasa(rezervare),
        getPret(rezervare),
        getCheckin(rezervare)
    )






