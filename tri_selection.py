# Création de la fonction de tri sélection 
def tri_selection(tab):
    comparaison_selection = 0
    echanges_selection = 0

    # Boucle qui parcourt la longueur du tableau donné
    for i in range(len(tab) - 1):

        min = i

        # Boucle qui compare la valeur prise en minimum à l'ensemble des valeurs du tableau
        for j in range(i+1, len(tab)):
            if tab[min] > tab[j]:
                echanges_selection += 1
                comparaison_selection += 1
                min = j
                
            else:
                comparaison_selection += 1
                
        tempo = tab[i]
        tab[i] = tab[min]
        tab[min] = tempo
    
    affectation_selection = echanges_selection * 3 
    return tab, comparaison_selection, echanges_selection, affectation_selection