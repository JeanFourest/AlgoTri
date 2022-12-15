def tri_insertion(tab): 
    for i in range(1, len(tab)): 
        k = tab[i] 
        j = i-1
        while j >= 0 and k < tab[j] : 
                tab[j + 1] = tab[j] 
                j -= 1
        tab[j + 1] = k
tab = [45, 2, 56, 3, 8, 9, 10]
tri_insertion(tab) 
print ("Le tableau trié est:")
