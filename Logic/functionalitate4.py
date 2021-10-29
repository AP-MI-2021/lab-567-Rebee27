from Domain.companie_aeriana import getClasa, getPret


def pretMaxim(lista):
    '''
    Determinarea prețului maxim pentru fiecare clasă
    param lista: lista de rezervari
    return: pretul maxim pentru fiecare clasa
    '''
    lista_max = {}
    for rezervare in lista:
        clasa = getClasa(rezervare)
        pret = getPret(rezervare)
        if clasa in lista_max:
            if pret > lista_max[clasa]:
                lista_max[clasa] = pret
        else:
            lista_max[clasa] = pret

    return lista_max