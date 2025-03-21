nb = int(input("Donne un nombre "))
produit = 1
impaire = []

for i in range(nb):
     impaire.append(2 * i+1)
     produit *= (2 * i+1)

print(f"les {nb} premier nombre impaires sont {impaire}")

print(f"Le produit des {nb} premiers nombres impairs est {produit}")