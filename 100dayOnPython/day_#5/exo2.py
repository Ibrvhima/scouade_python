numberInSeconds = int(input("Donner nous un  nombre en (s) ..."))
h = numberInSeconds // 3600
sRestant = numberInSeconds % 3600
m = sRestant // 60
sRestant = sRestant % 60 

print(f"{numberInSeconds}s = {h}h:{m}min:{sRestant}s")
