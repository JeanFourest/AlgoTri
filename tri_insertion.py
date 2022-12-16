from copy import copy
def tri_insertion(tab):
    
    copie_insertion = copy(tab)
    
    echanges_insertion = 0
    comparaisons_insertion = 0
    
    for i in range(1, len(copie_insertion)):
        k = copie_insertion[i]
        j = i - 1
        while j >= 0 and k < copie_insertion[j]:
            copie_insertion[j + 1] = copie_insertion[j]
            j -= 1
            echanges_insertion += 1
            comparaisons_insertion += 1
        copie_insertion[j + 1] = k
        comparaisons_insertion += 1
        
        
    affectations_insertion = echanges_insertion * 3
    operation_insertion = affectations_insertion + comparaisons_insertion
    return operation_insertion