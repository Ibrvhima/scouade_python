nbr = int(input("Donner un nombre "))
somme = 0

for i in range(1, nbr + 1):
     somme += i**2

print(f"la somme des carre de 1 à N est: {somme}")