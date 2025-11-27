
temp = int(input("Enter temperature in °C: "))

if temp < 0:
    print("Freezing conditions")
elif temp < 10:
    print("Cold")
elif temp < 25:
    print("Warm")
else:
    print("Hot")