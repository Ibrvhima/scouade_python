PHT = int(input("Entrer un prix hors tac(HT) "))
TVA = float(input(("Entrer la TVA en %  ")))

mtva = PHT * TVA/100
pttc = PHT + mtva

print(f"Le prix TTC est {pttc:.2f} gnf")