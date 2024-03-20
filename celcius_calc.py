temp = float(input("Enter a temperature: "))
if temp < -273.15:
    print(temp, "is invalid because it is below absolute zero")
elif temp == -273.15:
    print("The temperatureis at absolute zero")
elif -273.15 < temp < 0:
    print("Temperature is below freezing point")
elif temp == 0:
    print("Temperature is at the freezing point")
elif 0 < temp < 100:
    print("Temperature is at normal range")
elif temp == 100:
    print("Temperature is at boiling point")
else:
    print("Temperature is above the boiling point")