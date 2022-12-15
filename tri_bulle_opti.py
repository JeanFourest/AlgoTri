def tri_bulle_opti(list):
    
    permut = True

    #compteurs pour les comparaisons et échanges qui seront afficher à la fin de la fonction
    comparaisons_tri_bulle_opti = 0
    echanges_tri_bulle_opti = 0

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

                comparaisons_tri_bulle_opti += 1
                echanges_tri_bulle_opti += 3

            else:

                comparaisons_tri_bulle_opti += 1

    #affiche les compteurs
    print(f'nombre de comparaisons: {comparaisons_tri_bulle_opti}')
    print(f"nombre d'échanges/affectations: {echanges_tri_bulle_opti}")

    return list