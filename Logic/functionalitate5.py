from Domain.companie_aeriana import getPret


def ordonareDescrescatoare(lista):
    '''
    ordonarea rezervarilor descrescator dupa pret
    param lista: lista de rezervari
    return: lista ordonata descrescator dupa pret
    '''

    lista_preturi = []

    for rezervare in lista:
        lista_preturi.append(rezervare)

    lista_preturi.sort(key=getPret, reverse=True)

    return lista_preturi

