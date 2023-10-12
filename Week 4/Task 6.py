celc = "a"
while not celc.isdigit():
    celc = input("Please enter a celsius value ")

fahr = (int(celc) * 1.8) + 32
print(str(celc) + "°C in fahrenheit is " + str(fahr) + "°F.")