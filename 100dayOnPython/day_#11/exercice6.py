# 7. Vérifie si une clé existe dans un dictionnaire.

mon_dict = {
     "nom" : 'alice',
     "age" : 22,
     "ville" : "Paris"
}

check = "noma" in mon_dict
print(check)

# 8. Modifie la valeur d'une clé dans un dictionnaire.

mon_dict["age"] = 33
print(mon_dict)

# 9. Utilise la méthode .get() pour accéder à un élément du dictionnaire.
print(mon_dict.get("nom"))