# Création de la fonction de tri sélection 
def tri_selection(tab):
    compteur = 0
    for i in range(len(tab) - 1):

        min = i

        for j in range(i+1, len(tab)):
            if tab[min] > tab[j]:
                min = j

        tempo = tab[i]
        tab[i] = tab[min]
        tab[min] = tempo
        
    return tab

tab = [69, 10, 20, 6, 4, 12]

print(tri_selection(tab))