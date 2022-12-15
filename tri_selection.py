# Création de la fonction de tri sélection 
def tri_selection(tab):

    # Boucle qui parcourt la longueur du tableau donné
    for i in range(len(tab)):

        min = i

        # Boucle qui compare la valeur prise en minimum à l'ensemble des valeurs du tableau
        for j in range(i+1, len(tab)):
            if tab[min] > tab[j]:
                min = j

        
        tempo = tab[i]
        tab[i] = tab[min]
        tab[min] = tempo
        
    return tab