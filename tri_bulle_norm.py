def tri_bulle_norm(list):

    echanges = 0
    comparaisons = 0

    long_tableau = len(list)

    for i in range(long_tableau - 1):

        for j in range(0, long_tableau - i - 1):

            if list[j] > list[j + 1]:

                list[j], list[j + 1] = list[j + 1], list[j]

                echanges += 1

                comparaisons += 1

            else:
                comparaisons += 1

    affectation = echanges * 3
    return list, comparaisons, echanges, affectation