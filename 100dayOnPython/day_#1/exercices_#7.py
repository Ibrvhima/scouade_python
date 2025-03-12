temperatureCelcuis = float(input("Donner une temperature en °c "))

temperatureFharenthein = (temperatureCelcuis * 9/5) + 32
temperatureKelvin = temperatureCelcuis + 273.15

print(f"{temperatureCelcuis} °C = {temperatureFharenthein} °F")
print(f"{temperatureCelcuis} °C = {temperatureKelvin} °K")
