def tri_bulle_opti(list):

    echanges_bulle_opti = 0
    comparaisons_bulle_opti = 0
    
    #longueur du tableau
    long_tableau = len(list)

    #fait les comparaisons
    for i in range(long_tableau - 1):
        for j in range(0, long_tableau - i - 1):

            #si nombre 1 est supérieure au nombre 2 alors faire l'échange
            if list[j] > list[j + 1]:

                list[j], list[j + 1] = list[j + 1], list[j]

                #les compteurs
                echanges_bulle_opti += 1
                comparaisons_bulle_opti += 1

            else:
                comparaisons_bulle_opti += 1

    affectation_bulle_opti = echanges_bulle_opti * 3

    #retourne les résusltats
    return list, comparaisons_bulle_opti, echanges_bulle_opti, affectation_bulle_opti