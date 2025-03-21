number = int(input('donner un nombre '))
pair =[]

for i in range(1, number+1):
     if i % 2 == 0:
          pair.append(i)
print(f"les nombre paire de 1 à {number} sont {pair}")