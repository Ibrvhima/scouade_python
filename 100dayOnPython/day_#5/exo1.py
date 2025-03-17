sentense = input("Entrer du text ici... ")
voyelles = "aeiouyAEIOUY"
vCounter = 0
cCounter = 0


for i in sentense:
     if i in voyelles:
         vCounter += 1

for j in sentense:
     if j.isalpha() and j not in voyelles:
          cCounter += 1

print(f"({sentense} ) contient {vCounter} voyelles et {cCounter} consonne ")