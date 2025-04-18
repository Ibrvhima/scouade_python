myListe = [1,2,3,7,6,5,4,9,8,7]

myListe.sort()
print(myListe)

n = len(myListe)

milieu = n // 2

if n % 2 == 0:
      mediane = (myListe[milieu - 1] + myListe[milieu]) / 2
     
else:
      mediane = myListe[milieu]
    

print(f"la mediane est {mediane}")
