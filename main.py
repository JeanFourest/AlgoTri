import tri_bulle_norm 
import tri_bulle_opti 
import tri_insertion 
import tri_selection 
from random import randint

tab = [273, 8732, 81, 0, 823, 6, 354, 12, 56]

print(tri_selection.tri_selection(tab))
print(tri_insertion.tri_insertion(tab))
print(tri_bulle_norm.tri_bulle_norm(tab))
print(tri_bulle_opti.tri_bulle_opti(tab))