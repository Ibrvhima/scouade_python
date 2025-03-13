number = int(input("Donner un nombre "))

numberConverse = str(number)
counterNumber = 0
for i in numberConverse:
     counterNumber += 1

print(f"{numberConverse} contient {counterNumber} chiffre(s)")

# Deuxieme methode
nombre = int(input("Donner un nombre "))
print(f"le nombre {nombre} contient {len(number)} chiffres")