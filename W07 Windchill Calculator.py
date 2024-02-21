def calculateChill(T,V):
    chill = 35.74 + (0.6215 * T) - (35.75 * (V ** 0.16)) + (0.4275 * T * (V ** 0.16))
    print(f"At temperature {T:.1f}F, and wind speed {V} mph, the windchill is: {chill:.2f}F")

def celsiusConversion(celsius):
    convertedTemp = celsius * (9/5) + 32
    return convertedTemp


temperature = float(input("What is the temperature? "))

while True:
    unit = input("Fahrenheit or Celsius (F/C)? ")
    if unit.lower() != "f" and unit.lower() != "c":
        print("Invalid input.")
    else:
        break

if unit.lower() == "c":
    temperature = celsiusConversion(temperature)

speed = 0
while speed < 60:
    speed += 5
    calculateChill(temperature, speed)