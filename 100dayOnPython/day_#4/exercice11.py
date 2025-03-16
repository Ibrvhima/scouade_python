heigth = float(input("Donner votre taille en (cm)  ")) / 100
weight = float(input("Donner votre poids en kg  "))

imc = weight / (heigth * heigth)

print(f"Votre masse corporelle est de {imc: .2f}")