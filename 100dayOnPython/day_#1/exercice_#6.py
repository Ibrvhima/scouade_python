nb = int(input("Donner un nombre "))
somme = 0

for i in range(1, nb + 1):
     somme += i


print(f"la somme des nombre de 1 à {nb} est {somme}")

n = int (input("donner un autre nombre "))

somme = (n *(n + 1))// 2

print(f"la somme de n nombre de 1 à {n} est {somme}")
