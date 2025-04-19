# 1. Crée un set contenant les nombres de 1 à 5.

monSet = {1,2,3,4,5}

# 2. Ajoute un nombre supplémentaire (par exemple, 6) au set.
monSet.add(6)
print(monSet)

# 3. Essaie d’ajouter un élément déjà présent et observe ce qui se passe.
monSet.add(2)
print(monSet)

# 4. Crée deux sets et fais l’union, l’intersection et la différence entre eux.
set1 = {2,3,4}
set2 = { 3,4,5}

union = set1 | set2
print(union)

# 5. Vérifie si un élément est présent dans un set avec l’opérateur in.

checkin = 2 in set2
print(checkin)

# creation d'un set vide
setVide = set()

# 7. Utilise la méthode .remove() pour supprimer un élément d’un set.
deleting = set2.remove(5)
print(set2)

# 8. Utilise la méthode .discard() pour supprimer un élément d’un set sans erreur si l'élément n'existe pas.

discard = set1.discard(2)

print(discard)

ma_liste = [1, 2, 2, 3, 4, 5, 6, 7]
new_set = set(ma_liste)
print(new_set)

# 10. Trouve la taille d’un set avec la fonction len().

print(len(new_set))