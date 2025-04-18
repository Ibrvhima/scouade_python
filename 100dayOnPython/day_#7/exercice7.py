nbr = int(input("Donner un nombre : "))
somme = 0

while nbr > 0:
     reste = nbr % 10
     somme += reste
     nbr //= 10
print(f"la somme est {somme}")

