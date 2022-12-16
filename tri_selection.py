from copy import copy
# Création de la fonction de tri sélection 
def tri_selection(tab):
    
    copie_selection = copy(tab)
    
    comparaison_selection = 0
    echanges_selection = 0

    # Boucle qui parcourt la longueur du tableau donné
    for i in range(len(copie_selection) - 1):

        min = i

        # Boucle qui compare la valeur prise en minimum à l'ensemble des valeurs du tableau
        for j in range(i+1, len(copie_selection)):
            if copie_selection[min] > copie_selection[j]:
                echanges_selection += 1
                comparaison_selection += 1
                min = j
                
            else:
                comparaison_selection += 1
                
        tempo = copie_selection[i]
        copie_selection[i] = copie_selection[min]
        copie_selection[min] = tempo
    
    affectation_selection = echanges_selection * 3 
    operation_selection = affectation_selection + comparaison_selection
    return operation_selection

