def tri_bulle_norm(list):

    echanges = 0
    comparaisons = 0
    
    #longueur du tableau
    long_tableau = len(list)

    #fait les comparaisons
    for i in range(long_tableau - 1):
        for j in range(0, long_tableau - i - 1):

            #si nombre 1 est supérieure au nombre 2 alors faire l'échange
            if list[j] > list[j + 1]:

                list[j], list[j + 1] = list[j + 1], list[j]

                #les compteurs
                echanges += 1
                comparaisons += 1

            else:
                comparaisons += 1

    affectation = echanges * 3

    #retourne les résusltats
    return list, comparaisons, echanges, affectation