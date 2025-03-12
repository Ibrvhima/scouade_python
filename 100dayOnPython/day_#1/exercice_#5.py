number1 = int(input("donner un premier nombre "))
number2 = int(input("donner un second nombre "))
if number1 > number2:
     print(f"{number1} est plus grand que {number2}")
elif number1 < number2:
     print(f"{number2} est plus grand que {number1}")
else:
     print(f"{number1} est égal à {number2}")