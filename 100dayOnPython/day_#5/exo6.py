chaine = input("Donner un text et voir s'il commence par une voyelle  ")

if chaine:
     firstChar = "aeiouyAEIOUY"
     if chaine[0] in firstChar:
         print(f"{chaine} commence bien par une voyelle😊")
     else:
         print(f"{chaine} ne commence par une voyelle🤦‍♂️")
else:
    print("vous avez saisi un chaine vide")

