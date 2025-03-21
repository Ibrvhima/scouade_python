nbr = int(input("Donner un nombre "))

print(f"les diviseur de {nbr} sont:", end=" ")
for i in range(1, nbr +1):
     if nbr % i == 0:
          print(i, end=" ")