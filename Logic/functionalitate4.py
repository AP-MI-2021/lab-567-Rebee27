from Domain.companie_aeriana import getClasa, getPret


def pretMaxim(lista):
    '''
    Determinarea prețului maxim pentru fiecare clasă
    param lista: lista de rezervari
    return: pretul maxim pentru fiecare clasa
    '''
    lista_max = []
    max_economy = 0
    max_economy_plus = 0
    max_business = 0
    for rezervare in lista:
        if getClasa(rezervare) == "economy":
            if getPret(rezervare) >max_economy:
                max_economy = getPret(rezervare)
        elif getClasa(rezervare) == "economy plus":
            if getPret(rezervare) > max_economy_plus:
                max_economy_plus = getPret(rezervare)
        elif getClasa(rezervare) == "business":
            if getPret(rezervare) > max_business:
                max_business = getPret(rezervare)

    lista_max.append(max_economy)
    lista_max.append(max_economy_plus)
    lista_max.append(max_business)
    return lista_max