nbr = int(input("Donner un nombre "))
somme = 0
for i in range(1, nbr):
     if nbr % i == 0:
          somme += i
     
if somme == nbr:
     print(f"{nbr} est un nombre parfait🆗 ")
else:
     print(f"{nbr} n'est pas un nombre parfait🙆‍♀️")