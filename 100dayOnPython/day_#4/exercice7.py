price = int(input("Donner le prix d'un produit "))
prom = float(input("Donner un pourcentage de reduction "))

prixPromotion = (prom / 100) * price

print(f"le prix après reduction est : {price - prixPromotion}")