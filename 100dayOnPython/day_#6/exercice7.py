nb1 = int(input("Donner le premier nombre : "))
nb2 = int(input("Donner le deuxième nombre : "))
nb3 = int(input("Donner le troisième nombre : "))

if nb1 > nb2 and nb1 > nb3:
    print(f'Le plus grand est {nb1}')
elif nb2 > nb1 and nb2 > nb3:
    print(f'Le plus grand est {nb2}')
else:
    print(f'Le plus grand est {nb3}')

