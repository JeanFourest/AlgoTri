from copy import copy
def tri_bulle_norm(list):
    
    copie_bulle_norm = copy(list)
    
    permut = True

    #compteurs pour les comparaisons et échanges qui seront afficher à la fin de la fonction
    comparaisons_bulle_norm = 0
    echanges_bulle_norm = 0

    repetition = 0
    #si permut == True alors faire les échanges nécessaire
    while permut == True:

        permut = False

        repetition += 1
        #boucle qui parcourt la longueur du tableau donné
        for i in range(0, len(copie_bulle_norm) - repetition):
            #si le nombre 1 est superieure au nombre 2 alors échanger
            if copie_bulle_norm[i] > copie_bulle_norm[i + 1]:

                permut = True
                # l'échange se passe ici
                copie_bulle_norm[i], copie_bulle_norm[i + 1] = copie_bulle_norm[i + 1], copie_bulle_norm[i]

                comparaisons_bulle_norm += 1
                echanges_bulle_norm += 1

            else:

                comparaisons_bulle_norm += 1
                permut = True
                
    affectation_bulle_norm = echanges_bulle_norm * 3
    operation_bulle_norm = affectation_bulle_norm + comparaisons_bulle_norm

    return operation_bulle_norm