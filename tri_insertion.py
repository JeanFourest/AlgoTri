def tri_insertion(tab):
    
    echanges_insertion = 0
    comparaisons_insertion = 0
    
    for i in range(1, len(tab)):
        k = tab[i]
        j = i - 1
        
        while j >= 0 and k < tab[j]:
            tab[j + 1] = tab[j]
            j -= 1
            echanges_insertion += 1
            comparaisons_insertion += 1
        comparaisons_insertion += 1
        tab[j + 1] = k
        
        
    affectations_insertion = echanges_insertion * 3    
    return tab, comparaisons_insertion, echanges_insertion, affectations_insertion