import tri_bulle_norm 
import tri_bulle_opti 
import tri_insertion 
import tri_selection 
import random

def stat(min, max, step, nbr):
    
    contenant = []
    moyenne = 0
    somme = 0

    print("Voici les différents tris \n Tri par sélection (1) \n Tri par insertion (2) \n Tri à bulle normal (3) \n Tri à bulle optimisé (4) \n")
    choix = int(input("Quel tri choisissez vous ? : "))
    
    while min <= max:
        
        # Boucle qui crée le nombre de tableau demandée grâce au paramètre nbr
        for i in range(nbr):
            
            # Ajout du nombre exacte de valeurs, de façon aléatoire, dans un tableau, puis le stocke dans un autre tableau
            tab = [random.randint(0,100) for i in range(min)]
            contenant.append(tab)
            
        for i in range(len(contenant)):
            if choix == 1:
                tri = tri_selection.tri_selection(contenant[i])
            elif choix == 2:
                tri = tri_insertion.tri_insertion(contenant[i])
            elif choix == 3:
                tri = tri_bulle_norm.tri_bulle_norm(contenant[i])
            elif choix == 4:
                tri = tri_bulle_opti.tri_bulle_opti(contenant[i])
            somme += tri
            
        moyenne = somme / min
        print(min, round(moyenne, 1))
        min += step

stat(10, 20, 5, 10)
