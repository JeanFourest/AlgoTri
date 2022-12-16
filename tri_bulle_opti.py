from copy import copy
def tri_bulle_opti(list):
    
    copie_bulle_opti = copy(list)

    echanges_bulle_opti = 0
    comparaisons_bulle_opti = 0
    
    #longueur du tableau
    long_tableau = len(copie_bulle_opti)

    #fait les comparaisons
    for i in range(long_tableau - 1):
        for j in range(0, long_tableau - i - 1):

            #si nombre 1 est supérieure au nombre 2 alors faire l'échange
            if copie_bulle_opti[j] > copie_bulle_opti[j + 1]:

                copie_bulle_opti[j], copie_bulle_opti[j + 1] = copie_bulle_opti[j + 1], copie_bulle_opti[j]

                #les compteurs
                echanges_bulle_opti += 1
                comparaisons_bulle_opti += 1

            else:
                comparaisons_bulle_opti += 1

    affectation_bulle_opti = echanges_bulle_opti * 3
    operation_bulle_opti = affectation_bulle_opti + comparaisons_bulle_opti

    #retourne les résusltats
    return operation_bulle_opti