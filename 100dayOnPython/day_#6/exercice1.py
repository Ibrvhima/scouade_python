number = int(input("DOnner un entier "))
i = 0

while i * i <= number:
     if i * i == number:
          estCarreParfait = True
          break

     i += 1
if estCarreParfait:
     print(f"{number} est un carré parfait")
else:
     print(f"{number} n'est pas un carre parfait")