def tri_bulle_opti(list):
    
    permut = True

    #compteurs pour les comparaisons et échanges qui seront afficher à la fin de la fonction
    comparaisons_bulle_opti = 0
    echanges_bulle_opti = 0

    repetition = 0
    #si permut == True alors faire les échanges nécessaire
    while permut == True:

        permut = False

        repetition += 1
        #boucle qui parcourt la longueur du tableau donné
        for i in range(0, len(list) - repetition):
            #si le nombre 1 est superieure au nombre 2 alors échanger
            if list[i] > list[i + 1]:

                permut = True
                # l'échange se passe ici
                list[i], list[i + 1] = list[i + 1], list[i]

                comparaisons_bulle_opti += 1
                echanges_bulle_opti += 1

            else:

                comparaisons_bulle_opti += 1
                
    affectation_bulle_opti = echanges_bulle_opti * 3

    return list, comparaisons_bulle_opti, echanges_bulle_opti, affectation_bulle_opti