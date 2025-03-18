distance = float(input("Donner une distance "))
vitesse = float(input('Donner une vitesse '))

if vitesse == 0:
     print("La vitesse doit etre non null🤦‍♂️")

else:
     temp = distance / vitesse

     print(f"Pour une distance de {distance}m avec une vitesse de {vitesse}m/s le temp du trajet sera {temp}s")